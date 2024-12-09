import datetime
import numpy as np
from tabulate import tabulate


# Data setup
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
time_slots = ["08:30-09:45", "09:45-11:00", "11:00-12:15","12:15-01:30",  "01:30-02:45", "02:45-04:00", "04:00-05:15"]

# Class 1: TimetableGenerator
class TimetableGenerator:
    def __init__(self, days, time_slots):
        self.days = days
        self.time_slots = time_slots
        self.timetable = {}  # Dictionary to hold timetable data

    def generate_timetable(self):
        # Initialize timetable with "Free" slots
        for day in self.days:
            self.timetable[day] = {}
            for slot in self.time_slots:
                self.timetable[day][slot] = "Free"

        # Predefined schedule data
        predefined_schedule = {
            "Saturday": {
                "08:30-09:45": "Database Management System - CSE311 (MSJ)",
                "09:45-11:00": "Software Project III - CSE316 (MHN)",
                "11:00-12:15": "Computer Networks - CSE313 (CSA)",
                "01:30-02:45": "Introduction to Data Science - CSE315 (FFZ)",
                "02:45-04:00": "Computer Architecture - CSE335 (MAIT)"
            },
            "Sunday": {
                "08:30-09:45": "Database Management System Lab - CSE312 (MSJ)",
                "09:45-11:00": "Computer Networks Lab - CSE314 (CSA)",
                "11:00-12:15": "Object-Oriented Programming II - CSE221 (NIB)",
                "12:15-01:30": "Computer Architecture - CSE335 (MAIT)",
                "04:00-05:15": "Introduction to Data Science - CSE315 (FFZ)"
            },
            "Monday": {
                "09:45-11:00": "Object-Oriented Programming II Lab - CSE222 (NIB)",
                "11:00-12:15": "Object-Oriented Programming II Lab - CSE222 (NIB)"
            },
            "Wednesday": {
                "08:30-09:45": "Computer Networks Lab - CSE314 (CSA)",
                "11:00-12:15": "Database Management System Lab - CSE312 (MSJ)",
                "12:15-01:30": "Database Management System - CSE311 (MSJ)",
                "04:00-05:15": "Database Management System Lab - CSE312 (MSJ)"
            },
            "Thursday": {
                "09:45-11:00": "Computer Networks - CSE313 (CSA)",
                "01:30-02:45": "Object-Oriented Programming II Lab - CSE222 (NIB)",
                "02:45-04:00": "Object-Oriented Programming II Lab - CSE222 (NIB)",
                "04:00-05:15": "Object-Oriented Programming II Lab - CSE222 (NIB)"
            }
        }

        # Adding predefined schedule to the timetable
        for day, slots in predefined_schedule.items() :
            for time_slot, subject in slots.items():
                self.timetable[day][time_slot] = subject

        return self.timetable

    def display_day_routine(self, day):
        if day in self.timetable:
            print(f"Routine for {day} :")
            for slot, subject in self.timetable[day].items():
                print(f"{slot} : {subject}")
        else:
            print(f"No schedule available for {day}.")

    def print_timetable(self):
        print("Full Timetable :")
        for day, slots in self.timetable.items():
            print(f"{day} :")
            for slot, subject in slots.items():
                print(f"  {slot} : {subject}")

    def display_timetable(self):
        for day, slots in self.timetable.items():
            print(f"{day}:")
            print("+--------------+-------------------+-----------------------------------------+------------+")
            print("|    Time      |    Course Code    |               Course Title              |  Teacher   |")
            print("+--------------+-------------------+-----------------------------------------+------------+")
            for slot, subject in slots.items():
                course_code, course_title, teacher = self.parse_subject(subject)
                print(f"| {slot:<12} | {course_code:<17} | {course_title:<39} | {teacher:<10} |")
                print("+--------------+-------------------+-----------------------------------------+------------+")

    def parse_subject(self, subject):
        if subject == "Free":
            return ("-", "Free", "-")
        parts = subject.split(" - ")
        if len(parts) > 1:
            course_code = parts[1].split("(")[0].strip()
            course_title = parts[0].strip()
            teacher = parts[1].split("(")[1].replace(")", "").strip()
            return (course_code, course_title, teacher)
        return ("Unknown", subject, "Unknown")

# Class 2 : ClassSchedule (Handles each class schedule)
class ClassSchedule:
    def __init__(self, class_name):
        self.class_name = class_name

    def set_class(self, timetable, day, time_slot, course_code, course_title, teacher_name):
        try:
            if timetable[day][time_slot] == "Free":
                # Correctly format the subject string
                timetable[day][time_slot] = f"{course_title} - {course_code} ({teacher_name})"
                print(f"Class '{course_title} - {course_code} ({teacher_name})' assigned to {day} at {time_slot}.")
            else:
                print(f"Slot {time_slot} on {day} is already occupied.")
        except KeyError as e:
            print(f"Error: {e}. Please check the day or time slot.")

# Class 3 : Subject
class Subject :
    def __init__(self):
        pass

    def Take_courseCode(self) :
        print("Enter the course code : ", end=" ")
        self.course_code = input().strip().upper()
        return self.course_code

    def Take_CourseTitle(self) :
        print("Enter the course title : ", end=" ")
        self.course_title = input().strip().title()
        return self.course_title

# Class 4 : Teacher (Handles teacher details)
class Teacher:
    def __init__(self):
        pass
    def Take_Teacher_initial(self) :
        print("Enter the teacher's initials : ", end=" ")
        self.teacher_name = input().strip().upper()
        return self.teacher_name

# Class 5: Day (Represents a day of the week)
class Day :
    def __init__(self) :
        pass
    def Get_for_single_day(self) :
        print("Enter the day : ", end=" ")
        self.day = input().strip().capitalize()
        return self.day

    def Get_day(self) :
        print("Enter the day : ", end=" ")
        self.day = input().strip().capitalize()
        while self.day not in days :
            print("Invalid day. Please try again.")
            self.day = input().strip().capitalize()

        return self.day

# Class 6: TimeSlot (Represents a time slot in the timetable)
class TimeSlot:
    def __init__(self) :
        pass
    def Get_timeSlot(self) :
        self.free_slots = [slot for slot in timetable[day] if timetable[day][slot] == "Free"]
        print(f"Available free slots: {free_slots}")
        print("Enter the time slot: ", end=" ")
        self.time_slot = input().strip()
        while self.time_slot not in free_slots:
            print("Invalid or occupied slot. Please choose from the available free slots.")
            time_slot = input().strip()

        return self.time_slot

# Class 7 : Class Inheritance
class OnlineClass(ClassSchedule):  # Inherits from ClassSchedule
    def __init__(self) :
       pass

    def get_class_info(self) :
        print("By default Your class is scheduled offline")
        print("Do you want to fix it online ? (yes/no) : ", end=" ")
        self.a = input().lower()
        if self.a == "yes" :
            print("Your class is now scheduled online")
            return
        else :
            return

# Class 8 : Custom Exception for Invalid Day or Slot
class TimetableException(Exception) :
    def __init__(self, message) :
        self.message = message
        super().__init__(self.message)

# Class 9: Helper methods for Date handling   
class DateHelper :
    def __init__(self) :
        pass

    @staticmethod
    def get_current_date():
        return datetime.date.today()

 # Class 10: Polymorphism Example for Different Class Types
class ClassInfo(TimetableGenerator, Day, DateHelper) :
    def __init__(self) :
        pass

    def display_info(self) :
        print("Do you want a single day routine or weekly? (write yes for single day) : ", end=" ")
        self.a = input().lower()
        if self.a == "yes" :
            print("For Today or others ? (to for today) :",end=" ")
            self.x = input().strip().lower()
            if self.x == "to" :
                self.today_1 = super().get_current_date()
                super().display_day_routine(self.today_1)

            else :
                self.s_day = super().Get_for_single_day()
                super().display_day_routine(self.s_day)

        else :
            print("Table format or normal ? (yes or no) :",end=" ")
            self.b = input().lower()
            if self.b == "yes" :
                super.display_timetable()
            else :
                super.print_timetable()

# Class 11: Iterator Example for Iterating through the timetable
class TimetableIterator :
    def __init__(self, timetable) :
        self.timetable = timetable
        self.day_index = 0
        self.slot_index = 0

    def __iter__(self) :
        return self

    def __next__(self) :
        if self.day_index < len(self.timetable):
            current_day = list(self.timetable.keys())[self.day_index]
            current_slot = list(self.timetable[current_day].keys())[self.slot_index]
            result = (current_day, current_slot, self.timetable[current_day][current_slot])
            self.slot_index += 1
            if self.slot_index >= len(self.timetable[current_day]):
                self.slot_index = 0
                self.day_index += 1
            return result
        else :
            raise StopIteration


# Class 12 : Using NumPy for timetable data manipulation
class TimetableAnalysis :
    def __init__(self, timetable) :
        self.timetable = timetable

    def count_free_slots(self):
        # Count how many 'Free' slots are there
        free_count = 0
        for day in self.timetable :
            for slot in self.timetable[day] :
                if self.timetable[day][slot] == "Free":
                    free_count += 1
        return free_count

# Class 13 : Lambda Function
class TimetableLambda(DateHelper):
    def __init__(self):
        self.check_free = lambda day, slot: "Free" if timetable[day][slot] == "Free" else "Occupied"
    
    def is_slot_available(self, day, slot):
        return self.check_free(day, slot)

# Welcome message
print("\nWelcome to the Timetable Management System!\n")

C_info = ClassInfo()

    # Create timetable generator
timetable_gen = TimetableGenerator(days, time_slots)
timetable = timetable_gen.generate_timetable()

    # Display full timetable
timetable_gen.display_timetable()
timetable_analysis = TimetableAnalysis(timetable)
sub = Subject()
teacher = Teacher()
d = Day()
ts = TimeSlot()
oc = OnlineClass()
tl = TimetableLambda()

while True :
    free_slots = timetable_analysis.count_free_slots()
    print(f"\nNumber of free slots available: {free_slots}")
    print("\nWould you like to assign or remove a class? (assign/remove/exit) : ", end=" ")
    choice = input().strip().lower()
    if choice == "assign":
        day = d.Get_day()

        course_code = sub.Take_courseCode()

        course_title = sub.Take_CourseTitle()

        print(f"Free slots for {day}: ", end=" ")
        free_slots = [slot for slot in timetable[day] if timetable[day][slot] == "Free"]
        if not free_slots:
            print(f"No free slots on {day}. Please choose another day.")
            continue

        time_slot = ts.Get_timeSlot()
        print("The slot is ",tl.check_free(day, time_slot))

        teacher_name = teacher.Take_Teacher_initial()

        oc.get_class_info()

        # Assign the class with course code, title, and teacher name
        class_schedule = ClassSchedule(course_title)
        class_schedule.set_class(timetable, day, time_slot, course_code, course_title, teacher_name)

    elif choice == "remove":
        day = d.Get_day()

        print(f"Slots for {day} :")
        for time_slot, subject in timetable[day].items():
            print(f"{time_slot}: {subject}")

        print("Enter the time slot to remove : ", end=" ")
        time_slot = input().strip()
        while time_slot not in timetable[day]:
            print("Invalid slot. Please try again.")
            time_slot = input().strip()

        # Remove the class
        if timetable[day][time_slot] != "Free":
            print(f"Removing class '{timetable[day][time_slot]}' from {day} at {time_slot}.")
            timetable[day][time_slot] = "Free"
        else:
            print(f"Slot {time_slot} on {day} is already free.")

    elif choice == "exit":
        print("Exiting the class assignment/removal process.")
        break
    else:
        print("Invalid input. Please enter 'assign', 'remove', or 'exit'.")

# Display updated timetable after all operations
print("\nFinal Updated Timetable :")
timetable_gen.display_timetable()
print()

# Creating an instance of TimetableIterator
timetable_iterator = TimetableIterator(timetable)

# Iterate through the timetable using the iterator
for day, slot, subject in timetable_iterator:
    print(f"{day} - {slot}: {subject}")