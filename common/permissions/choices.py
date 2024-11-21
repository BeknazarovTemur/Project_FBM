from django.db import models


class Permissions(models.TextChoices):
    MODIFY_COMPANY_DATA = 'modify_company_data'
    ADD_COMPANY_EMPLOYEE = 'add_company_employee'
    ADD_COMPANY_ROLE = 'add_company_role'
