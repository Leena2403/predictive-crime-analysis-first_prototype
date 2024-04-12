# This suggests the deployment plans based on the beat that is provided.

import csv
import pandas as pd

file_path = 'cluster_dict.csv'
df = pd.read_csv(file_path)

def get_cluster_lists(beat_name, FIR_Details_Data, cluster_dict):
    cluster_list = {
        0: [
            "Establish specialized cybercrime investigation units within law enforcement agencies equipped with the necessary expertise, technology, and resources to investigate offenses under the Information Technology Act. These units should consist of trained cybercrime investigators, forensic analysts, and legal experts.",
            "Provide regular training and capacity building programs for law enforcement personnel to enhance their understanding of cyber laws, digital forensics, and emerging cyber threats. Collaborate with cybersecurity experts, academic institutions, and industry partners to develop tailored training modules and workshops.",
            "Establish dedicated cybercrime reporting mechanisms, such as helplines, online portals, and mobile applications, to enable victims to report cyber offenses easily and seek assistance from law enforcement agencies. Ensure that reporting channels are accessible, user-friendly, and capable of handling confidential information securely.",
            "Invest in state-of-the-art digital forensics laboratories equipped with advanced technology and tools for collecting, preserving, and analyzing digital evidence related to cybercrimes. Ensure that forensic examiners are trained to handle various types of digital evidence, including computers, mobile devices, and network logs.",
            "Launch public awareness campaigns to educate individuals and organizations about cybersecurity best practices, common cyber threats, and their legal rights and responsibilities under the Information Technology Act. Promote safe online behavior, password hygiene, and the importance of securing personal and sensitive information.",
            "Deploy dedicated cyber patrols and investigative teams to monitor online activities, identify potential threats, and conduct proactive investigations into cybercrimes. Utilize advanced cybersecurity tools, surveillance techniques, and data analytics to detect and deter cyber threats in real-time.",
            "Provide legal support and guidance to victims of cybercrimes throughout the investigation and prosecution process. Work closely with prosecutors, legal experts, and judicial authorities to ensure timely and effective prosecution of cyber offenders under the provisions of the Information Technology Act."
        ],
        1: [
            "Allocate additional police patrols to areas with a history of simple hurt incidents, such as nightlife districts, crowded public spaces, and areas prone to gang-related violence. Ensure that officers are vigilant and responsive to any signs of potential altercations.",
            "Implement community engagement programs to build trust and cooperation between law enforcement agencies and local residents. Encourage community members to report incidents of simple hurt promptly and provide information to assist in investigations.",
            "Improve street lighting in areas where simple hurt crimes are prevalent to enhance visibility and deter criminal activity during nighttime hours. Ensure that poorly lit areas are adequately illuminated to increase public safety and reduce the likelihood of confrontations.",
            "Deploy mobile police units equipped with medical supplies and trained personnel to respond quickly to incidents of simple hurt. Ensure that these units have the capability to provide immediate first aid to victims and transport them to medical facilities if necessary.",
            "Establish victim support services to provide assistance and counseling to individuals who have experienced simple hurt offenses. Ensure that victims are aware of their rights and have access to resources to help them recover from their injuries and seek justice.",
            "Implement outreach programs targeted at at-risk youth populations to provide mentorship, education, and alternative activities to prevent involvement in violent behavior. Engage youth in positive recreational activities and empower them to become agents of change in their communities."
            ],
        2: [
            "Increase police presence in areas prone to criminal activities, particularly during peak hours and weekends.",
            "Install CCTV cameras in strategic locations to monitor suspicious activities and provide evidence for investigations.",
            "Deploy mobile units equipped with necessary resources to respond quickly to incidents reported on highways or remote areas.",
            "Develop informer networks and utilize technology for intelligence gathering to identify and apprehend repeat offenders.",
            "Conduct targeted raids based on actionable intelligence to dismantle criminal networks operating in the area.",
            "Provide support services for victims of crime, including counseling and legal assistance, to encourage reporting and ensure justice.",
            "Regularly train police personnel in modern investigative techniques and equip them with the necessary skills to handle different types of crimes effectively.",
            "Utilize data analytics to identify crime hotspots and trends, enabling proactive policing strategies to prevent crimes before they occur."],
        3: [
            "Implement increased surveillance measures in areas prone to crimes against security for good behavior. Utilize CCTV cameras, drones, and other monitoring technologies to closely monitor public spaces and identify suspicious behavior.",
            "Conduct undercover sting operations to catch individuals involved in crimes against security for good behavior. Deploy plainclothes officers to observe and apprehend offenders engaged in illegal activities, such as soliciting bribes or extortion.",
            "Strengthen internal affairs divisions within law enforcement agencies to investigate allegations of corruption or misconduct among police officers and public officials. Ensure transparency and accountability in law enforcement practices to maintain public trust and integrity.",
            "Establish mechanisms to protect whistleblowers who report incidents of corruption or misconduct within law enforcement agencies and government institutions. Ensure confidentiality and immunity for individuals who come forward with credible information to expose wrongdoing.",
            "Implement policies and procedures to promote transparency and accountability in government operations, including financial transactions, procurement processes, and regulatory enforcement. Publish information on government spending and contracts to deter corruption and promote public scrutiny.",
            "Create specialized task forces dedicated to investigating and prosecuting crimes against security for good behavior. Equip these units with the resources and authority needed to conduct thorough investigations and hold perpetrators accountable for their actions."
            ],
        4: [
            "Deploy dedicated patrol units equipped with motorcycles or three-wheelers to monitor areas with high incidents of crimes against two-wheelers and three-wheelers. These units should conduct regular patrols and respond swiftly to reports of theft, vandalism, or other criminal activities targeting vehicles.",
            "Encourage the use of vehicle tracking systems and anti-theft devices on two-wheelers and three-wheelers to deter theft and facilitate recovery in case of theft. Provide incentives or subsidies for installing GPS trackers, alarms, and immobilizers on vehicles.",
            "Establish community watch programs involving residents, vehicle owners, and local businesses to collectively safeguard against crimes targeting two-wheelers and three-wheelers. Encourage citizens to report suspicious activities and share information with law enforcement authorities.",
            "Conduct sting operations to catch individuals engaged in the theft, resale, or illicit trade of stolen two-wheelers and three-wheelers. Use bait vehicles equipped with tracking devices to lure thieves and apprehend them in the act.",
            "Establish specialized investigation units within law enforcement agencies to handle cases related to crimes against two-wheelers and three-wheelers. Provide training and resources to investigators to conduct thorough inquiries and gather evidence for successful prosecutions."
            ],
        5: [
            "Deploy additional police patrols along national highways to deter criminal activities and provide a visible presence to travelers.",
            "Set up regular traffic checkpoints along national highways to inspect vehicles, verify identities, and detect any illegal substances or contraband being transported.",
            "Establish mobile command centers equipped with surveillance cameras and communication systems to monitor activity along national highways and coordinate rapid responses to incidents.",
            "Work closely with highway authorities to identify high-risk areas and implement measures such as improved lighting, signage, and road barriers to enhance safety and security.",
            "Engage with local communities living near national highways to encourage vigilance and prompt reporting of suspicious activities or individuals.",
            "Utilize technology such as CCTV cameras, license plate recognition systems, and GPS tracking to monitor traffic flow and detect suspicious behavior or vehicles.",
            "Establish protocols for coordinated responses to emergencies and criminal incidents on national highways, involving law enforcement agencies, emergency services, and highway authorities."],
        6: [
            "Deploy additional police patrols in areas with high incidents of crimes against women, such as public transportation hubs, parks, alleys, and poorly lit streets. Ensure that officers are visible and accessible to deter potential offenders.",
            "Implement community policing initiatives where officers engage directly with residents to build trust and gather information about potential threats to women's safety. Encourage community members to report suspicious activities and provide support to victims.",
            "Establish specialized units within the police force dedicated to addressing crimes against women, such as sexual assault and domestic violence units. These units should consist of trained officers who handle cases sensitively and provide support to victims throughout the legal process.",
            "Provide comprehensive training to law enforcement officers on gender sensitivity, victim support services, and relevant laws pertaining to crimes against women. Ensure that officers are equipped with the necessary skills to handle cases involving women with empathy and professionalism.",
            "Enhance existing helpline services dedicated to assisting women in distress. Ensure that helplines are staffed with trained personnel who can provide immediate support, guidance, and referral services to victims of violence.",
            "Partner with non-governmental organizations (NGOs) and women's rights groups to provide additional support services to victims, including counseling, legal aid, and shelter facilities. Collaborate on awareness campaigns to educate the public about women's rights and available support services.",
            "Implement measures to enhance the safety of public transportation for women, such as increasing the number of female police officers on buses and trains, installing CCTV cameras, and establishing designated waiting areas with adequate lighting.",
            "Enforce a zero-tolerance policy towards crimes against women, including prompt investigation and prosecution of offenders. Send a strong message that perpetrators will face severe consequences for their actions to deter future incidents."
            ],
        7: [
            "Deploy additional police patrols along state highways during peak crime hours to deter criminal activity and ensure rapid response to incidents.",
            "Establish strategic checkpoints at entry and exit points of state highways to monitor incoming and outgoing traffic, conduct vehicle inspections, and identify suspicious individuals or vehicles.",
            "Collaborate with highway authorities to implement joint patrols and surveillance efforts, leveraging their expertise in monitoring traffic flow and identifying potential crime hotspots.",
            "Deploy mobile command centers equipped with advanced communication and surveillance technology to strategic locations along state highways, enabling real-time coordination and response to emerging threats.",
            "Engage with local communities residing along state highways to build trust, gather intelligence, and encourage citizen participation in reporting suspicious activities or crimes.",
            "Conduct regular traffic enforcement operations targeting traffic violations and unsafe driving behaviors on state highways, which can help prevent accidents and deter criminal activity.",
            "Install visible signage along state highways advising travelers to remain vigilant, secure their belongings, and report suspicious activities to law enforcement authorities.",
            "Launch public awareness campaigns through media channels, roadside billboards, and community events to educate motorists and travelers about safety tips, emergency procedures, and reporting mechanisms while using state highways."],
        8: [
            "Implement community policing programs where officers engage with local residents and businesses to build trust, gather intelligence, and address concerns specific to each neighborhood.",
            "Identify high-crime areas on other roads and establish strategic patrol routes to increase police visibility and deter criminal activity.",
            "Focus enforcement efforts on specific types of crimes commonly occurring on other roads, such as theft, vandalism, or illegal dumping.",
            "Install surveillance cameras in key locations along other roads to monitor activity and gather evidence for investigations.",
            "Establish quick response teams equipped to swiftly react to reports of suspicious activity or emergencies on other roads, ensuring a rapid and effective police response.",
            "Set up a dedicated hotline or online reporting system for residents to report crimes or suspicious behavior on other roads, enabling law enforcement to act promptly on community tips.",
            "Implement environmental design strategies such as improved lighting, landscaping, and signage to enhance the safety and security of other roads and surrounding areas.",
            "Provide specialized training to officers on patrolling techniques, crime prevention strategies, and community engagement skills tailored to the unique challenges of policing other roads."],
        9: [
            "Establish specialized task forces dedicated to investigating and preventing cheating-related crimes. These task forces should comprise trained personnel with expertise in fraud detection and investigation.",
            "Implement surveillance and monitoring systems to track suspicious activities related to cheating. Utilize CCTV cameras, electronic surveillance, and data analysis tools to identify patterns and trends indicative of cheating behavior.",
            "Collaborate with educational institutions to implement measures to prevent cheating in exams and assessments. Provide training to educators on proactive measures and technology-enabled solutions to curb cheating.",
            "Conduct sting operations to catch individuals engaged in cheating schemes, such as selling counterfeit products, providing fraudulent services, or participating in academic dishonesty. Use decoys and bait to lure offenders into incriminating themselves.",
            "Invest in technology solutions to combat cheating, such as anti-plagiarism software, biometric authentication systems, and secure online examination platforms. Leverage advancements in technology to detect and prevent cheating in various domains.",
            "Engage the community in efforts to combat cheating by encouraging whistleblowing and reporting suspicious activities. Establish hotlines and anonymous reporting mechanisms to enable citizens to report instances of cheating confidentially.",
            "Provide ongoing training and development opportunities for law enforcement personnel to enhance their skills in investigating cheating-related crimes. Stay updated on emerging trends and tactics used by cheaters to stay ahead of the curve."],
        10: [
            "Increase community policing efforts in areas where incidents of security for good behavior are prevalent. Establish closer ties with local residents and community leaders to gather intelligence and foster trust.",
            "Deploy visible police patrols in neighborhoods and public areas to deter individuals from engaging in behavior that warrants security for good behavior orders. Regular patrols can help maintain order and address issues promptly.",
            "Focus enforcement efforts on individuals known to engage in disruptive behavior or criminal activities that may lead to security for good behavior orders. Use proactive policing strategies such as surveillance and targeted interventions.",
            "Develop early intervention programs targeting at-risk individuals, such as youth involved in delinquent behavior or individuals with a history of minor offenses. Provide mentorship, counseling, and support services to redirect behavior and prevent escalation."],
        11: [
            "Deploy dedicated teams of law enforcement officers to conduct regular patrols in areas known for the violation of the Karnataka Excise Act 1965. Focus on locations such as bars, pubs, liquor shops, and areas prone to illegal alcohol production and distribution.",
            "Establish a robust intelligence network to gather information on individuals and establishments involved in violating the Karnataka Excise Act. Utilize informants, undercover agents, and surveillance techniques to identify illegal alcohol manufacturing units, bootleggers, and distributors."
            "Organize coordinated raids on suspected premises where violations of the Excise Act are suspected to occur. Conduct surprise inspections of liquor shops, bars, and warehouses to check for compliance with licensing regulations and illegal alcohol sales.",
            "Strengthen border surveillance measures to prevent the smuggling of illicit liquor across state borders. Collaborate with neighboring states and law enforcement agencies to monitor and intercept illegal alcohol transportation routes.",
            "Educate the community about the adverse effects of illegal alcohol consumption and the importance of adhering to the provisions of the Karnataka Excise Act. Encourage citizens to report any instances of illegal alcohol production, sale, or consumption to the authorities.",
            "Conduct regular inspections to verify the licenses of establishments selling alcohol. Ensure that liquor vendors, distributors, and manufacturers comply with the legal requirements outlined in the Karnataka Excise Act and its regulations.",
            "Leverage technology solutions such as surveillance cameras, drones, and data analytics to enhance enforcement efforts. Monitor online platforms and social media channels for any indications of illegal alcohol sales or promotion.",
            "Provide specialized training to law enforcement personnel on the provisions of the Karnataka Excise Act and effective enforcement techniques. Equip officers with the knowledge and skills necessary to identify and respond to violations promptly.",
            "Foster collaboration between law enforcement agencies and the Karnataka Excise Department to streamline enforcement efforts. Share information, coordinate operations, and conduct joint initiatives to combat violations of the Excise Act effectively."],
        12: [
            "Deploy plainclothes officers in areas known for street gambling to conduct undercover operations and gather evidence.",
            "Increase foot patrols in streets and alleys where street gambling activities are prevalent to deter offenders and reassure the public.",
            "Utilize surveillance cameras strategically placed in areas prone to street gambling to monitor suspicious activities and gather evidence for prosecution.",
            "Collaborate with local community leaders and stakeholders to gather intelligence on street gambling operations and gather support for enforcement efforts.",
            "Conduct regular raids on suspected street gambling dens to disrupt illegal activities and send a clear message of zero tolerance.",
            "Form specialized task forces composed of trained officers to investigate and dismantle organized street gambling networks operating within the region.",
            "Partner with other law enforcement agencies and relevant government departments to coordinate efforts and share resources in combating street gambling effectively."],
        13: [
            "Deploy surveillance cameras in areas prone to breaches of Security for Good Behaviour. Monitor these cameras in real-time and review footage to identify suspicious behavior and individuals.",
            "Establish strong community policing initiatives to foster trust between law enforcement agencies and residents. Encourage community members to report any instances of breaching security for good behavior promptly.",
            "Conduct regular patrols in neighborhoods and public spaces to deter potential violators of Security for Good Behaviour. Maintain a visible presence to deter criminal activity and respond swiftly to any breaches.",
            "Conduct targeted enforcement operations to apprehend individuals who are known to violate Security for Good Behaviour. Use intelligence-led policing techniques to identify hotspots and target repeat offenders.",
            "Implement diversion programs and rehabilitation services for individuals who have been convicted of breaching Security for Good Behaviour. Offer support and resources to help them reintegrate into society and avoid future criminal activity.",
            "Launch public awareness campaigns to educate residents about the importance of maintaining security for good behavior in their communities. Encourage them to report any suspicious behavior and work together to keep their neighborhoods safe.",
            "Utilize technology such as mobile applications and online reporting systems to streamline the process of reporting breaches of Security for Good Behaviour. Enable residents to report incidents quickly and anonymously, facilitating faster response times."
        ],
        14: [
            "Deploy law enforcement officers strategically in areas prone to crimes against public safety, such as crowded public spaces, transportation hubs, and entertainment venues. Ensure regular foot patrols, bike patrols, and vehicle patrols to deter criminal activity and respond quickly to emergencies.",
            "Create specialized units within law enforcement agencies to focus on crimes against public safety, such as gangs, drug trafficking, and organized crime. Equip these units with the necessary resources, including intelligence gathering tools, surveillance equipment, and undercover officers, to target high-risk individuals and criminal organizations.",
            "Conduct targeted enforcement operations to address specific crime trends and hotspots affecting public safety. Utilize data-driven approaches to identify high-crime areas and deploy resources accordingly. Collaborate with other law enforcement agencies and community partners to maximize impact and disrupt criminal networks.",
            "Implement CPTED principles to enhance the safety and security of public spaces. Assess the design and layout of urban areas, parks, transportation facilities, and residential neighborhoods to identify potential vulnerabilities and implement measures to minimize opportunities for criminal activity, such as improved lighting, surveillance cameras, and landscaping.",
            "Ensure law enforcement agencies are adequately prepared to respond to emergencies and critical incidents that threaten public safety, such as natural disasters, terrorist attacks, and mass shootings. Conduct regular training exercises, drills, and simulations to test response protocols and enhance coordination with other emergency responders, including fire departments, EMS, and government agencies.",
            "Provide comprehensive victim support services to individuals and communities affected by crimes against public safety. Offer trauma-informed care, counseling, legal assistance, and financial support to help victims recover from their experiences and rebuild their lives. Collaborate with local organizations and service providers to ensure victims receive the support they need.",
            "Leverage technology to enhance public safety efforts, including surveillance cameras, license plate recognition systems, gunshot detection sensors, and predictive analytics software. Invest in innovative solutions to improve situational awareness, intelligence gathering, and crime prevention capabilities."
        ],
        15: [
            "Infiltrate Matka dens with plainclothes officers to gather intelligence and evidence on illegal gambling activities.",
            "Utilize surveillance cameras and other monitoring technologies to track suspicious activities related to Matka gambling, including monitoring known gambling hotspots.",
            "Conduct regular raids on Matka dens to disrupt operations and arrest individuals involved in illegal gambling activities.",
            "Work closely with local communities to raise awareness about the negative impacts of gambling and encourage residents to report suspicious activities.",
            "Pursue legal action against individuals and organizations involved in Matka gambling, prosecuting offenders to the fullest extent of the law.",
            "Establish an intelligence-gathering network to collect information on Matka gambling networks, targeting high-value individuals and dismantling entire gambling networks.",
            "Work with other law enforcement agencies to investigate the financial aspects of Matka gambling and identify any links to organized crime or corruption.",
            "Pursue asset seizure and forfeiture against individuals found guilty of participating in Matka gambling, confiscating assets obtained through illegal activities.",
            "Block access to gambling websites and apps to deter individuals from participating in online Matka gambling, collaborating with internet service providers and technology companies."],
        16: [
            "Deploy additional police patrols in areas known for criminal intimidation incidents. Ensure officers are visible and accessible to deter potential offenders and reassure the community.",
            "Provide specialized training for law enforcement officers on how to recognize signs of criminal intimidation and effectively respond to such incidents. Equip them with conflict resolution skills and de-escalation techniques to handle tense situations.",
            "Establish victim support services to assist individuals who have been subjected to criminal intimidation. Provide them with counseling, legal aid, and other resources to help them cope with the trauma and pursue justice.",
            "Conduct targeted enforcement operations to apprehend individuals known for engaging in criminal intimidation. Use intelligence-led policing techniques to identify hotspots and repeat offenders.",
            "Utilize technology such as surveillance cameras, mobile applications for reporting incidents, and data analytics to gather intelligence on criminal intimidation patterns and trends. Leverage social media platforms to disseminate safety tips and encourage community participation in crime prevention efforts."
        ],
        17: [
            "Deploy additional police patrols and surveillance in areas with a history of crimes against men, such as public transportation hubs, entertainment districts, and secluded alleys. Ensure that officers are visible and readily available to respond to incidents promptly.",
            "Conduct undercover operations to gather intelligence and apprehend perpetrators of crimes against men, such as muggings or assaults. Use plainclothes officers to monitor suspicious activities and apprehend offenders in the act.",
            "Foster stronger relationships between law enforcement agencies and local communities to encourage cooperation and information sharing. Organize community forums and neighborhood watch programs to empower residents to report crimes and work together to address safety concerns.",
            "Implement targeted enforcement actions against known offenders and criminal networks involved in crimes against men. Use data-driven approaches to identify hotspots and patterns of criminal activity, allowing law enforcement to focus resources where they are most needed.",
            "Launch educational campaigns to raise awareness about common tactics used in crimes against men and provide tips for personal safety. Distribute informational materials and conduct workshops in schools, workplaces, and community centers to educate individuals on how to protect themselves from potential threats.",
            "Partner with social service agencies and non-profit organizations to provide support services to male victims of crime, including counseling, legal assistance, and emergency shelter. Ensure that victims have access to resources to help them recover from traumatic experiences and navigate the criminal justice system.",
            "Improve street lighting in high-crime areas frequented by men to enhance visibility and deter criminal activity during nighttime hours. Install motion-sensor lighting and CCTV cameras to increase surveillance and create a safer environment for pedestrians.",
            "Develop targeted outreach programs aimed at at-risk populations, such as homeless individuals, substance abusers, and marginalized communities. Provide access to social services, addiction treatment, and housing assistance to address underlying issues contributing to their vulnerability to crime.",
            "Offer self-defense training programs for men to empower them with the skills and confidence to protect themselves from potential threats. Partner with martial arts schools or self-defense instructors to provide workshops and classes tailored to the needs of different age groups and demographics."
            ]}

    # district_data = FIR_Details_Data[FIR_Details_Data['District_Name'] == district_name]
    beat_crimeheads = FIR_Details_Data[FIR_Details_Data['Beat_Name'] == beat_name]['CrimeHead_Name']
    max_crimehead = beat_crimeheads.value_counts().idxmax()
    cluster = cluster_dict[cluster_dict['crimehead'] == max_crimehead]['cluster'].values[0]
    suggestions = cluster_list.get(cluster, [])

    return max_crimehead, suggestions

