from django.shortcuts import render
from sikadahomesApp.models import *

# Create your views here.

def index(request):
    return render(request, 'admin-app/index.html')

def page_404(request):
    return render(request, 'admin-app/404.html')

def page_500(request):
    return render(request, 'admin-app/500.html')

def add_agent(request):
    return render(request, 'admin-app/add-agent.html')


def generate_random_id(length=10):
        import random
        import string
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))



def SaveFunction(request, param):    
        region = request.POST.get('region')
        budget = request.POST.get('budget')
        img_listing = request.FILES.get('img_listing')
        img_front = request.FILES.get('img_front')
        status = request.POST.get('status')
        price = request.POST.get('price')
        date = request.POST.get('date')
        property_title = request.POST.get('property_title')
        location = request.POST.get('location')
        property_address = request.POST.get('property_address')
        description = request.POST.get('description')
        property_name = request.POST.get('property_name')
        home_area = request.POST.get('home_area')
        rooms = request.POST.get('rooms')
        baths = request.POST.get('baths')
        year_built = request.POST.get('year_built')
        neigbourhood = request.POST.get('neigbourhood')
        lot_dimensions = request.POST.get('lot_dimensions')
        beds = request.POST.get('beds')
        balcony = request.POST.get('balcony')
        furnished = request.POST.get('furnished')
        completed = request.POST.get('completed')
        living_room = request.POST.get('living_room')
        dining_area = request.POST.get('dining_area')
        garden = request.POST.get('garden')
        gym = request.POST.get('gym')
        img_gallery_1 = request.FILES.get('img_gallery_1')
        img_gallery_2 = request.FILES.get('img_gallery_2')
        img_gallery_3 = request.FILES.get('img_gallery_3')
        air_conditioner = request.POST.get('air_conditioner') == 'on'
        pool = request.POST.get('pool') == 'on'
        wifi = request.POST.get('wifi') == 'on'
        near_church = request.POST.get('near_church') == 'on'
        near_estate = request.POST.get('near_estate') == 'on'
        dish_washer = request.POST.get('dish_washer') == 'on'
        security = request.POST.get('security') == 'on'
        indoor_game = request.POST.get('indoor_game') == 'on'
        cable_tv = request.POST.get('cable_tv') == 'on'
        microwave = request.POST.get('microwave') == 'on'
        # print(f''' Region = {region}, budget = {budget}, img_listing = {img_listing}, img_front = {img_front}, status = {status},
        #      price = {price}, date = {date} , property_title = {property_title},
        #      property_address = {property_address},  description = {description} , property_name = {property_name} ,
        #      home_area = {home_area}, rooms = {rooms}, baths = {baths},
        #      year_built = {year_built}, neigbourhood = {neigbourhood}, lot_dimensions={lot_dimensions},
        #      beds={beds},  balcony={balcony}, furnished={furnished}, completed={completed},
        #      living_room={living_room}, dining_area={dining_area}, garden={garden}, gym={gym}, img_gallery_1={img_gallery_1},
        #      img_gallery_2={img_gallery_2}, img_gallery_3={img_gallery_3}, air_conditioner={air_conditioner},     
        #      pool={pool}, wifi={wifi}, near_church={near_church}, near_estate={near_estate}, dish_washer={dish_washer}, security={security},
        #      indoor_game={indoor_game}, cable_tv={cable_tv}, microwave={microwave}
        #     ''') 
        property_id = generate_random_id()
        if param == 'house_for_sale':          
            a = HouseSale(property_id=property_id,location=location,
                          region=region,budget=budget,img_listing=img_listing,img_front=img_front,
                          status=status,price=price,date=date,property_title=property_title,property_address=property_address,description=description,
                          property_name=property_name,home_area=home_area,rooms=rooms,baths=baths,year_built=year_built,neigbourhood=neigbourhood,
                          lot_dimensions=lot_dimensions,beds=beds,balcony=balcony,furnished=furnished,completed=completed,living_room=living_room,
                          dining_area=dining_area,garden=garden,gym=gym,img_gallery_1=img_gallery_1,img_gallery_2=img_gallery_2,img_gallery_3=img_gallery_3,
                          air_conditioner=air_conditioner,pool=pool,wifi=wifi,near_church=near_church,near_estate=near_estate,dish_washer=dish_washer,
                          security=security,indoor_game=indoor_game,cable_tv=cable_tv,microwave=microwave,
                          )            
            a.save()
            
        elif param == 'house_for_rent':    
            a = HouseRent(property_id=property_id,location=location,
                          region=region,budget=budget,img_listing=img_listing,img_front=img_front,
                          status=status,price=price,date=date,property_title=property_title,property_address=property_address,description=description,
                          property_name=property_name,home_area=home_area,rooms=rooms,baths=baths,year_built=year_built,neigbourhood=neigbourhood,
                          lot_dimensions=lot_dimensions,beds=beds,balcony=balcony,furnished=furnished,completed=completed,living_room=living_room,
                          dining_area=dining_area,garden=garden,gym=gym,img_gallery_1=img_gallery_1,img_gallery_2=img_gallery_2,img_gallery_3=img_gallery_3,
                          air_conditioner=air_conditioner,pool=pool,wifi=wifi,near_church=near_church,near_estate=near_estate,dish_washer=dish_washer,
                          security=security,indoor_game=indoor_game,cable_tv=cable_tv,microwave=microwave,
                          )
            a.save()
        else:    
            a = HouseLease(property_id=property_id,location=location,
                          region=region,budget=budget,img_listing=img_listing,img_front=img_front,
                          status=status,price=price,date=date,property_title=property_title,property_address=property_address,description=description,
                          property_name=property_name,home_area=home_area,rooms=rooms,baths=baths,year_built=year_built,neigbourhood=neigbourhood,
                          lot_dimensions=lot_dimensions,beds=beds,balcony=balcony,furnished=furnished,completed=completed,living_room=living_room,
                          dining_area=dining_area,garden=garden,gym=gym,img_gallery_1=img_gallery_1,img_gallery_2=img_gallery_2,img_gallery_3=img_gallery_3,
                          air_conditioner=air_conditioner,pool=pool,wifi=wifi,near_church=near_church,near_estate=near_estate,dish_washer=dish_washer,
                          security=security,indoor_game=indoor_game,cable_tv=cable_tv,microwave=microwave,
                          )
            a.save()
        b = AllProperties(property_id = property_id , property_type=f'house_{param}', price=price, location=region)
        b.save()    

def add_property_house(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        # status_text = status.split('_')[1].capitalize()
        SaveFunction(request, status)
                                                                                                                                        
    #     region = request.POST.get('region')
    #     budget = request.POST.get('budget')
    #     file = request.POST.get('file')
    #     print(region, budget, file)
        # print('Posting')
    return render(request, 'admin-app/add-property_house.html')

def add_property_land(request):
    return render(request, 'admin-app/add-property_land.html')

def agent(request):
    return render(request, 'admin-app/agent.html')

def agent_invoice(request):
    return render(request, 'admin-app/agent-invoice.html')

def apartment(request):
    return render(request, 'admin-app/apartment.html')

def blank(request):
    return render(request, 'admin-app/blank.html')

def blog_dashboard(request):
    return render(request, 'admin-app/blog-dashboard.html')

def blog_details(request):
    return render(request, 'admin-app/blog-details.html')

def blog_grid(request):
    return render(request, 'admin-app/blog-grid.html')

def blog_list(request):
    return render(request, 'admin-app/blog-list.html')

def blog_post(request):
    return render(request, 'admin-app/blog-post.html')

def chat(request):
    return render(request, 'admin-app/chat.html')

def contact(request):
    return render(request, 'admin-app/contact.html')

def events(request):
    return render(request, 'admin-app/events.html')

def file_dashboard(request):
    return render(request, 'admin-app/file-dashboard.html')

def file_documents(request):
    return render(request, 'admin-app/file-documents.html')

def file_images(request):
    return render(request, 'admin-app/file-images.html')

def file_media(request):
    return render(request, 'admin-app/file-media.html')

def forgot_password(request):
    return render(request, 'admin-app/forgot-password.html')

def image_gallery(request):
    return render(request, 'admin-app/image-gallery.html')

def invoices(request):
    return render(request, 'admin-app/invoices.html')

def locked(request):
    return render(request, 'admin-app/locked.html')

def mail_compose(request):
    return render(request, 'admin-app/mail-compose.html')

def mail_inbox(request):
    return render(request, 'admin-app/mail-inbox.html')

def mail_single(request):
    return render(request, 'admin-app/mail-single.html')

def map(request):
    return render(request, 'admin-app/map.html')

def office(request):
    return render(request, 'admin-app/office.html')

def page_offline(request):
    return render(request, 'admin-app/page-offline.html')

def pricing(request):
    return render(request, 'admin-app/pricing.html')

def profile(request):
    return render(request, 'admin-app/profile.html')

def property_detail(request):
    return render(request, 'admin-app/property-detail.html')

def property_list(request):
    return render(request, 'admin-app/property-list.html')

def property_list3(request):
    return render(request, 'admin-app/property-list3.html')

def property_list4(request):
    return render(request, 'admin-app/property-list4.html')

def reports(request):
    return render(request, 'admin-app/reports.html')

def search_results(request):
    return render(request, 'admin-app/search-results.html')

def shop(request):
    return render(request, 'admin-app/shop.html')

def sign_in(request):
    return render(request, 'admin-app/sign-in.html')

def sign_up(request):
    return render(request, 'admin-app/sign-up.html')

def timeline(request):
    return render(request, 'admin-app/timeline.html')

def sign_up(request):
    return render(request, 'admin-app/sign-up.html')

def villa(request):
    return render(request, 'admin-app/villa.html')

def widgets_app(request):
    return render(request, 'admin-app/widgets-app.html')

def widgets_data(request):
    return render(request, 'admin-app/widgets-data.html')
