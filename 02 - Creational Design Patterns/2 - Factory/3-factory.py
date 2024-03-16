"""
factory is a class responsable for creating objects (instances) 
"""

# example 1

from math import sin, cos


class Point:

    def __init__(self) -> None:
        self.x = None
        self.y = None


class PointFactory:

    @staticmethod
    def new_cartesian_point(x, y):
        p = Point()
        p.x = x
        p.y = y
        return p

    @staticmethod
    def new_polar_point(rho, theta):
        p = Point()
        p.x = rho * cos(theta)
        p.y = rho * sin(theta)
        return p


# example 1


class Report:

    class ReportFactory:
        @staticmethod
        def create_report(report_type):
            if report_type == "financial":
                return Report("Financial Report")
            elif report_type == "marketing":
                return Report("Marketing Report")
            else:
                raise ValueError("Unknown report type")

    def __init__(self, name):
        self.name = name

    def display(self):
        return f"Displaying {self.name}"


"""
The most popular approach between using a dedicated factory class and embedding a factory method or factory class inside the class 
that the objects will be created from largely depends on the specific requirements of the project, 
design goals, and the complexity of the object creation process.
However, generally speaking, using a dedicated factory class is often favored in many scenarios due to its flexibility,
scalability, and adherence to the principles of object-oriented 
"""

# client code


financial_report = Report.ReportFactory.create_report("financial")
print(financial_report.display())  # Output: Displaying Financial Report

marketing_report = Report.ReportFactory.create_report("marketing")
print(marketing_report.display())  # Output: Displaying Marketing Report
