import json

from django.core.management import BaseCommand
from django.db.transaction import atomic

from languages.models import OriginalWord, Translations

lang_ids = {
    "en": 21,
    "ru": 20,
    "uz": 19,
    "oz": 23,
}

home_catalog_id = 6


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("data_file", type=str)

    @atomic
    def handle(self, *args, **options):
        file_path = options["data_file"]
        with open(file_path, encoding="utf-8") as json_file:
            items = json.load(json_file)

        origins = []

        for item in items.keys():
            origins.append(
                OriginalWord(
                    catalog_id=home_catalog_id,
                    original_word=item,
                )
            )

        original_words = OriginalWord.objects.bulk_create(origins)

        translations = []
        for origin in original_words:
            for lang_key in lang_ids.keys():
                try:
                    translations.append(
                        Translations(
                            original_word=origin,
                            language_id=lang_ids[lang_key],  # KeyError possible here
                            translation_text=items[origin.original_word][lang_key],
                        )
                    )
                except KeyError as e:
                    print(
                        "KeyError: {} - Missing key "
                        "for language_id or translation_text",
                        e,
                    )
                    print(
                        "Original word: {}, lang_key: {}",
                        origin.original_word,
                        lang_key,
                    )
                except TypeError as e:
                    print(
                        "TypeError: {} - Possible NoneType or wrong type encountered", e
                    )
                    print(
                        "Original word: {}, lang_key: {}",
                        origin.original_word,
                        lang_key,
                    )
                except AttributeError as e:
                    print(
                        "AttributeError: {} - Invalid attribute in origin "
                        "or origin.original_word",
                        e,
                    )
                    print(
                        "Original word: {}, lang_key: {}",
                        getattr(origin, "original_word", "Unknown"),
                        lang_key,
                    )

        created_translations = Translations.objects.bulk_create(translations)

        print(f"created_translations: {len(created_translations)}")
