from django.shortcuts import render
from .models import CustomerForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def home(request):
    params = {}
    params['passagemf'] = "Mutual funds are investment vehicles that pool money from multiple investors to create a diversified portfolio of securities such as stocks bonds and other assets One of the main benefits of mutual funds is that they provide individual investors with access to professional management and expertise even with relatively small amounts of money.By investing in a mutual fund investors can benefit from the knowledge and experience of professional fund managers who carefully select and manage a diversified portfolio on behalf of the investors This diversification helps spread the risk across different investments reducing the impact of any single securitys performance on the overall portfolio Mutual funds also offer liquidity as investors can buy or sell their shares on any business day at the net asset value NAV price This provides flexibility and convenience for investors who may need to access their funds quickly Moreover mutual funds offer various types and investment strategies to suit different risk profiles and financial goals allowing investors to choose funds that align with their preferences and investment objectives Additionally mutual funds provide economies of scale enabling investors to benefit from lower transaction costs and access to a wide range of investment opportunities that may not be feasible for individual investors Overall mutual funds offer a convenient professionally managed and diversified investment option for individuals seeking longterm growth and investment diversification regardless of their investment knowledge or capital."



    params['passageins'] = "Health insurance provides financial protection and access to healthcare services, offering numerous benefits to individuals and families. It safeguards against exorbitant medical expenses by spreading the financial risk across a large pool of insured individuals. With health insurance, policyholders can avail themselves of a wide range of medical services, including preventive care, diagnostics, hospitalization, medications, and specialized treatments. Regular check-ups and screenings can help detect and address potential health issues at an early stage, contributing to better health outcomes. Additionally, health insurance often includes coverage for emergencies, ensuring prompt and necessary care during unexpected medical events. By having insurance, individuals gain the freedom to choose healthcare providers and facilities that best suit their needs, fostering personalized and quality care. Furthermore, many health insurance plans offer access to networks of healthcare professionals, making it easier to find and connect with doctors and specialists. Moreover, health insurance promotes a healthier lifestyle by encouraging preventive measures and wellness programs, fostering overall well-being. Ultimately, health insurance plays a vital role in promoting health equity by providing access to healthcare services for individuals from diverse socioeconomic backgrounds. By mitigating financial barriers, it ensures that everyone has the opportunity to receive necessary medical care, leading to improved health and a higher quality of life."

    params['passagemedi'] = "Mediclaim, also known as health insurance, is a financial protection plan that provides coverage for medical expenses incurred by individuals or families. It offers a range of benefits that play a crucial role in safeguarding one's health and financial well-being. Firstly, mediclaim policies cover hospitalization expenses, including room charges, doctor's fees, surgical procedures, and diagnostic tests. This ensures that individuals can access quality healthcare without worrying about the exorbitant costs involved. Additionally, mediclaim often includes coverage for outpatient treatments, such as consultations, medication, and preventive care, promoting regular health check-ups and early detection of diseases. Another significant benefit is the provision for pre- and post-hospitalization expenses, covering costs incurred before and after hospitalization, such as diagnostic tests, medications, and follow-up consultations. This comprehensive coverage minimizes the financial burden on policyholders and their families. Furthermore, mediclaim often extends to cover ambulance charges, maternity expenses, and critical illnesses, providing additional support during emergencies and significant life events. By choosing mediclaim, individuals can also avail of cashless treatment facilities, where the insurance company settles the bills directly with the network hospitals, eliminating the need for immediate out-of-pocket payments. Moreover, mediclaim policies may offer tax benefits, where premiums paid are eligible for tax deductions under certain sections of the income tax act. This encourages individuals to invest in health insurance and benefit from the financial incentives. Overall, mediclaim is a valuable investment that offers financial security, peace of mind, and timely access to healthcare services, making it an essential component of an individual's overall risk management and well-being."

    return render(request, "homepage.html", params)


def test_page(request):
     params = {}
     params['passagemf'] = "Mutual funds are investment vehicles that pool money from multiple investors to create a diversified portfolio of securities such as stocks bonds and other assets One of the main benefits of mutual funds is that they provide individual investors with access to professional management and expertise even with relatively small amounts of money.By investing in a mutual fund investors can benefit from the knowledge and experience of professional fund managers who carefully select and manage a diversified portfolio on behalf of the investors This diversification helps spread the risk across different investments reducing the impact of any single securitys performance on the overall portfolio Mutual funds also offer liquidity as investors can buy or sell their shares on any business day at the net asset value NAV price This provides flexibility and convenience for investors who may need to access their funds quickly Moreover mutual funds offer various types and investment strategies to suit different risk profiles and financial goals allowing investors to choose funds that align with their preferences and investment objectives Additionally mutual funds provide economies of scale enabling investors to benefit from lower transaction costs and access to a wide range of investment opportunities that may not be feasible for individual investors Overall mutual funds offer a convenient professionally managed and diversified investment option for individuals seeking longterm growth and investment diversification regardless of their investment knowledge or capital."



     params['passageins'] = "Health insurance provides financial protection and access to healthcare services, offering numerous benefits to individuals and families. It safeguards against exorbitant medical expenses by spreading the financial risk across a large pool of insured individuals. With health insurance, policyholders can avail themselves of a wide range of medical services, including preventive care, diagnostics, hospitalization, medications, and specialized treatments. Regular check-ups and screenings can help detect and address potential health issues at an early stage, contributing to better health outcomes. Additionally, health insurance often includes coverage for emergencies, ensuring prompt and necessary care during unexpected medical events. By having insurance, individuals gain the freedom to choose healthcare providers and facilities that best suit their needs, fostering personalized and quality care. Furthermore, many health insurance plans offer access to networks of healthcare professionals, making it easier to find and connect with doctors and specialists. Moreover, health insurance promotes a healthier lifestyle by encouraging preventive measures and wellness programs, fostering overall well-being. Ultimately, health insurance plays a vital role in promoting health equity by providing access to healthcare services for individuals from diverse socioeconomic backgrounds. By mitigating financial barriers, it ensures that everyone has the opportunity to receive necessary medical care, leading to improved health and a higher quality of life."

     params['passagemedi'] = "Mediclaim, also known as health insurance, is a financial protection plan that provides coverage for medical expenses incurred by individuals or families. It offers a range of benefits that play a crucial role in safeguarding one's health and financial well-being. Firstly, mediclaim policies cover hospitalization expenses, including room charges, doctor's fees, surgical procedures, and diagnostic tests. This ensures that individuals can access quality healthcare without worrying about the exorbitant costs involved. Additionally, mediclaim often includes coverage for outpatient treatments, such as consultations, medication, and preventive care, promoting regular health check-ups and early detection of diseases. Another significant benefit is the provision for pre- and post-hospitalization expenses, covering costs incurred before and after hospitalization, such as diagnostic tests, medications, and follow-up consultations. This comprehensive coverage minimizes the financial burden on policyholders and their families. Furthermore, mediclaim often extends to cover ambulance charges, maternity expenses, and critical illnesses, providing additional support during emergencies and significant life events. By choosing mediclaim, individuals can also avail of cashless treatment facilities, where the insurance company settles the bills directly with the network hospitals, eliminating the need for immediate out-of-pocket payments. Moreover, mediclaim policies may offer tax benefits, where premiums paid are eligible for tax deductions under certain sections of the income tax act. This encourages individuals to invest in health insurance and benefit from the financial incentives. Overall, mediclaim is a valuable investment that offers financial security, peace of mind, and timely access to healthcare services, making it an essential component of an individual's overall risk management and well-being."
     return render(request, "test.html", params)


def contact_us(request):
    return render(request, 'contactus.html')


def contactDataSubmit(request):
    error = None
    if request.method == "POST":
        name = request.POST['fname']
        email = request.POST['femail']
        phno = request.POST['fphno']
        services = request.POST.getlist('service[]')
        if not name:
            error = "Name Required"
        elif len(name) < 10:
            error = "Enter Full Name"

        if not email:
            error = "Email Required"
        try:
            validate_email(email)
        except ValidationError as e:
            error = "Enter Valid Email"
            print("bad email, details:", e)
        else:
            print("good email")

        print(name, email, phno, services)
        if error == None:
            customer = CustomerForm(
                name=name, email=email, phno=phno, services=services)
            customer.save()
            print("Data Saved")
            return render(request, 'homepage.html')

        else:
            print("Data Not Saved")
            return render(request, 'contactus.html', {"error": error, "name": name, "email": email, "phno": phno, "padding": '10px'})


def about(request):
    params = {}
    params['div1passage'] = "Kadlag Investment is a reputable and well-established financial planning firm with over 25 years of experience in the industry. With a track record of excellence, we have successfully served more than 2000 satisfied customers. Our expertise lies in wealth management, where we have efficiently managed over 100 crores in assets. At Kadlag Investment, we understand the importance of comprehensive financial planning. In addition to our wealth management services, we offer a range of solutions to meet our clients' diverse needs. Our services include mediclaim and insurance, ensuring that our customers have access to the necessary coverage for their health and financial security.With a team of highly skilled professionals, we provide personalized and tailored solutions to our clients. We take pride in our ability to understand our clients' financial goals and develop strategies that align with their aspirations. Our commitment to delivering exceptional service, coupled with our extensive experience and expertise, sets us apart as a trusted partner in financial planning.Choose Kadlag Investment for your financial needs and experience the peace of mind that comes with working with a reliable and customer-centric firm. We are dedicated to helping individuals and businesses achieve financial success, making us the preferred choice for those seeking expert financial guidance."

    params['aumdes'] = "Kadlag Investment is a leading financial firm specializing in asset management. With an impressive portfolio totaling 100 crores in assets under management, we have a proven track record of successfully growing our clients' wealth.Our top priority is client satisfaction, and we take great pride in our extensive base of happy customers."

    params['cusdes'] = "Kadlag Investment is a renowned investment firm with an impressive track record of serving over 2500 satisfied customers. With our expertise and commitment to excellence, we have become a trusted partner for individuals and businesses seeking reliable investment solutions."

    params['yeardes'] = "Dear valued clients and partners,We are thrilled to share with you that Kadlag Investment has reached a significant milestone in our journey. For over 25 years, we have been committed to providing exceptional investment services and expertise to our esteemed clients."

    return render(request, 'about.html', params)
