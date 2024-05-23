from ..services.periods import create_period_choices
class Helper:
  STATUS_CHOICES = [
      (1, "Activo"),
      (2, "Inactivo"),
      (3, "Eliminado"),
  ]

  PERIOD_CHOICES = create_period_choices()

  RESPONSIBLE_CHOICES = [
      (1, "Administrador"),
  ]

  TD_CHOICES = [
    (1, "text"),
    (2, "number"),
  ]


  DEPARTMENT_CHOICES = [
    (1, "Admin"),
    (2, "JA"),
    (3, "EG")
  ]


