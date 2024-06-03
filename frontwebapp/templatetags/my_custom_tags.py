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
                        <span class="company">{experience.company_name}, {experience.location}  ({experience.formatted_start_date} - {experience.formatted_end_date})</span>
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
                        <span class="company">{education.university}, {education.location}  ({education.formatted_start_date} - {education.formatted_end_date})</span>
                    </div>
                    <div class="timeline-body">
                        <p>{education. description}</p>
                        <p><b><u>Skills</u> - </b>{education.skills}</p>
                    </div>
                </div>
            </li>
        '''
    return mark_safe(output)


@register.simple_tag
def render_feature_matrix(features, cols=3):
    output = ''
    len_features = len(features)
    row_count = (len(features) + cols - 1) // cols
    for row in range(row_count):
        output += '<div class="row">'
        for col in range(cols):
            index = row * cols + col
            if index < len(features):
                feature = features[index]
                col_width = 12 if len_features == 1 else ( 6 if len_features == 2 else 12 // cols)
                icon_class = getattr(feature, 'icon', None)
                if not icon_class:
                    icon_class = 'icon-browser'
                output += f'''
                    <div class="col-md-{col_width} text-center">
                        <div class="feature-left">
                            <span class="icon">
                                <i class="{icon_class}"></i>
                            </span>
                            <div class="feature-copy">
                                <h3>{feature.technology}</h3>
                                <p>{feature.description}</p> 
                            </div>
                        </div>
                    </div>
                '''
        output += '</div>'
    return mark_safe(output)

@register.simple_tag
def render_internships(internships):
    output = ''
    for internship in internships:
        output += f'''
                <div class="row">
                    <div class="col-md-10 text-center col-padding animate-box">
                        <a href="{internship.web_link}" class="work" style="background-image: url(static/frontwebapp/images/{internship.bg_img})">
                            <div class="desc">
                                <div style="height: 500px; width: 1000px; overflow-x: scroll; white-space: nowrap;" style="align-self: center;">
                    
                    '''
        for image in internship.images.all():
            output += f'''<img src="{ image.image.url }" alt="{ internship.web_link }" style=" height: 500px; width: 1000px; margin-right: 10px;">;'''    
        output += f'''                        
                               </div>
                            </div>
                        </a>
                        <div class="fh5co-heading text-center">
                            <h3 style="font-size: 24px;
                                        font-weight: 400;
                                        color: #fff;">
                                Project Name
                            </h3>
                            <span style="font-size: 16px;
                                        color: rgba(255, 255, 255, 0.7);">
                                Illustration
                            </span>
                        </div>
                    </div>
                </div>
            '''
    return mark_safe(output)
    
@register.simple_tag
def render_projects(projects):
    output = ''
    row_count = 0
    row_open = False

    for project in projects:
        if row_count == 0:
            output += '<div class="row">'
            row_open = True

        output += f'''
            <div class="col-md-6">
                <div class="fh5co-blog animate-box">
                    <a href="{project.project_link}" class="blog-bg" style="background-image: url(static/frontwebapp/images/{project.image_url});"></a>
                    <div class="blog-text">
                        <span class="posted_on">{project.start_date} - {project.end_date}</span>
                        <h3><a href="{project.project_link}">{project.title}</a></h3>
                        <ul class="stuff">
        '''

        for item in project.descriptions.all():
            output += f'<li><p class="text-justify">{item.text}</p></li>'

        output += f'''
                        </ul>
                        <ul class="stuff">
                            <li><i class="icon-heart2"></i>{project.likes}</li>
                            <li><i class="icon-eye2"></i>{project.views}</li>
                        </ul>
                    </div>
                </div>
            </div>
        '''

        row_count += 1
        if row_count == 2:
            output += '</div>'
            row_count = 0
            row_open = False

    if row_open:
        output += '</div>'

    return mark_safe(output)
