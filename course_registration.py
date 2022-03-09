from course_bot import CourseBot

bot = CourseBot()

#login
username = "your username"
password = "your password"
bot.login_to_stars(username, password)

#wait for register time
register_time = "your course registration time"
#example: 2021-12-07 14:00
bot.wait_for_registration(register_time)

#load plans and add courses
while True:
    bot.load_plan(1)
    bot.add_course()
    bot.load_plan(2)
    bot.add_course()
    bot.load_plan(3)
    bot.add_course()