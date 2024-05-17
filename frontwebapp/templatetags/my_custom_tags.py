from django import template
from django.utils.safestring import mark_safe

register = template.Library()

inverted = False

@register.simple_tag
def render_experience(workexps):
    global inverted
    output = ''
    for experience in workexps:
        li_class = 'timeline-inverted animate-box' if inverted else 'animate-box timeline-unverted'
        inverted = not inverted
        output += f'''
            <li class="{li_class}">
                <div class="timeline-badge"><i class="icon-suitcase"></i></div>
                <div class="timeline-panel">
                    <div class="timeline-heading">
                        <h3 class="timeline-title">{experience.title}</h3>
                        <span class="company">{experience.company_name}, {experience.location}  ({experience.start_date} - {experience.end_date})</span>
                    </div>
                    <div class="timeline-body">
                        <p>{experience. description}</p>
                        <p><b><u>Skills</u> - </b>{experience.skills}</p>
                    </div>
                </div>
            </li>
        '''

    return mark_safe(output)

@register.simple_tag
def render_education(educations):
    output = ''
    global inverted
    for education in educations:
        li_class = 'timeline-inverted animate-box' if inverted else 'animate-box timeline-unverted'
        inverted = not inverted
        output += f'''
            <li class="{li_class}">
                <div class="timeline-badge"><i class="icon-suitcase"></i></div>
                <div class="timeline-panel">
                    <div class="timeline-heading">
                        <h3 class="timeline-title">{education.degree}</h3>
                        <span class="company">{education.university}, {education.location}  ({education.start_date} - {education.end_date})</span>
                    </div>
                    <div class="timeline-body">
                        <p>{education. description}</p>
                        <p><b><u>Skills</u> - </b>{education.skills}</p>
                    </div>
                </div>
            </li>
        '''
    return mark_safe(output)