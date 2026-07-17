# Decorator to convert output to lowercase
def lowercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.lower()
    return wrapper


class Certificate:
    def __init__(self, student_name):
        self.student_name = student_name

    @classmethod
    def create_certificate(cls, name):
        return cls(name)

    def __str__(self):
        return f"Certificate Holder: {self.student_name}"

    @lowercase_decorator
    def issue(self):
        return f"Congratulations {self.student_name}! You have successfully completed the course."


# Main Program
name = input("Enter student name: ")

certificate = Certificate.create_certificate(name)

print("\n", certificate)
print(certificate.issue())
