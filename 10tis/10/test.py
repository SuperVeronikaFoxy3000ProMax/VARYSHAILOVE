class TrapezoidCalculator:
    """Класс для вычисления площади трапеции."""

    def _validate_positive_number(self, value):
        """Валидация положительного числаю."""
        try:
            num = float(value)
            return num > 0
        except (ValueError, TypeError):
            return False

    def calculate_area(self, base1, base2, height):
        """
        Вычисляет площадь трапеции по формуле: S = (a + b) / 2 * h
        """

        if not all(self._validate_positive_number(x) for x in [base1, base2, height]):
            return "Ошибка: все значения должны быть положительными числами."
        
        try:
            a = float(base1)
            b = float(base2)
            h = float(height)

            area = (a + b) / 2 * h
            return round(area, 2)

        except ValueError as e:
            return f"Ошибка ввода: {str(e)}"

    def validate_input(self, value):
        """Проверяет корректность введенных данных."""
        return self._validate_positive_number(value)

if __name__ == "__main__":
    calc = TrapezoidCalculator()

    print("Калькулятор площади трапеции.")
    a = input("Введите длину первого основания: ")
    b = input("Введите длину второго основания: ")
    h = input("Введите высоту трапеции: ")

    result = calc.calculate_area(a, b, h)
    print(f"Площадь трапеции: {result}")