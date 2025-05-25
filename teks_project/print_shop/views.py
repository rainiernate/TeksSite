from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from .models import Service, Testimonial, Post, ContactRequest
from .forms import ContactForm

def home(request):
    services = Service.objects.all().order_by('order')[:6]  # Get top 6 services
    testimonials = Testimonial.objects.filter(active=True)
    recent_posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')[:3]  # Get latest 3 posts
    
    context = {
        'services': services,
        'testimonials': testimonials,
        'recent_posts': recent_posts,
    }
    return render(request, 'print_shop/home.html', context)

def about(request):
    return render(request, 'print_shop/about.html')

class ServiceListView(ListView):
    model = Service
    template_name = 'print_shop/services.html'
    context_object_name = 'services'
    ordering = ['order']

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'print_shop/service_detail.html', {'service': service})

class PostListView(ListView):
    model = Post
    template_name = 'print_shop/blog.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'print_shop/post_detail.html'

def post_detail_by_id(request, post_id):
    # For demo purposes, we'll create sample blog posts based on the ID
    # In a real application, you would fetch these from the database
    
    blog_posts = {
        1: {
            'title': 'Things we print',
            'content': '<p>At TEKS Services, we offer a wide range of printing services to meet all your business needs. From business cards and brochures to large format banners and signs, our state-of-the-art printing technology ensures high-quality results every time.</p>\n\n<p>Our printing services include:</p>\n\n<ul>\n<li>Business Cards</li>\n<li>Brochures and Flyers</li>\n<li>Postcards</li>\n<li>Posters and Banners</li>\n<li>Stationery</li>\n<li>Marketing Materials</li>\n<li>Custom Printing Solutions</li>\n</ul>\n\n<p>We use only the highest quality materials and the latest printing technology to ensure your printed materials look professional and make a lasting impression.</p>',
            'published_date': '2025-03-12',
            'image': 'https://images.unsplash.com/photo-1576633587382-13ddf37b1fc1?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80'
        },
        2: {
            'title': 'Table-Top Banners with an X-Frame',
            'content': '<p>Table-top banners with an X-frame are perfect for trade shows, retail displays, and events. These compact banners are easy to set up and provide excellent visibility for your brand or message.</p>\n\n<p>Benefits of X-Frame Table-Top Banners:</p>\n\n<ul>\n<li>Lightweight and portable</li>\n<li>Quick and easy setup</li>\n<li>Durable construction</li>\n<li>High-quality printing</li>\n<li>Affordable pricing</li>\n</ul>\n\n<p>Our table-top banners are printed on premium materials to ensure vibrant colors and sharp images. They come with a carrying case for easy transportation and storage.</p>',
            'published_date': '2020-11-12',
            'image': 'https://images.unsplash.com/photo-1563986768609-322da13575f3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80'
        },
        3: {
            'title': 'Self Mailers & Tabbing Rules',
            'content': '<p>The USPS has specific requirements for self-mailers to ensure they can be processed through automated equipment. Our team is well-versed in these regulations and will ensure your mailers comply with all postal requirements.</p>\n\n<p>Key USPS Requirements for Self-Mailers:</p>\n\n<ul>\n<li>Proper tab placement based on size and weight</li>\n<li>Minimum paper weight requirements</li>\n<li>Size restrictions</li>\n<li>Fold orientation guidelines</li>\n<li>Address placement specifications</li>\n</ul>\n\n<p>Working with TEKS Services ensures your self-mailers will meet all USPS requirements, saving you time and money by avoiding potential delays or additional postage costs.</p>',
            'published_date': '2020-11-02',
            'image': 'https://images.unsplash.com/photo-1566125882500-87e10f726cdc?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80'
        },
        4: {
            'title': 'What is Direct Mail and Why is it Important?',
            'content': '<p>Direct mail remains one of the most effective marketing channels, offering tangible connections with customers in an increasingly digital world.</p>\n\n<p>Benefits of Direct Mail Marketing:</p>\n\n<ul>\n<li>Higher response rates compared to email marketing</li>\n<li>Tangible presence in customers\'s homes or offices</li>\n<li>Highly targeted marketing capabilities</li>\n<li>Less competition in the mailbox than the inbox</li>\n<li>Builds brand recognition and trust</li>\n<li>Complements digital marketing efforts</li>\n</ul>\n\n<p>Our direct mail services include design, printing, mailing list management, and postal optimization to ensure your campaign achieves the best possible results.</p>',
            'published_date': '2020-10-30',
            'image': 'https://images.unsplash.com/photo-1512758017271-d7b84c2113f1?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80'
        },
        5: {
            'title': 'Wedding Announcements',
            'content': '<p>Your wedding announcement is an important part of your special day. We offer a variety of custom designs, paper options, and printing techniques to create beautiful wedding announcements that reflect your style and personality.</p>\n\n<p>Our Wedding Announcement Services Include:</p>\n\n<ul>\n<li>Custom design services</li>\n<li>Premium paper options</li>\n<li>Foil stamping and embossing</li>\n<li>Envelope addressing</li>\n<li>Mailing services</li>\n</ul>\n\n<p>We understand the importance of your wedding announcements and will work closely with you to create announcements that perfectly capture the spirit of your special day.</p>',
            'published_date': '2019-04-21',
            'image': 'https://images.unsplash.com/photo-1606761568499-6d2451b23c66?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80'
        }
    }
    
    # Get the blog post data or return a 404 if not found
    post = blog_posts.get(post_id)
    if not post:
        from django.http import Http404
        raise Http404("Blog post not found")
    
    # Create a context with the post data
    context = {
        'post': post,
    }
    
    return render(request, 'print_shop/post_detail.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_request = ContactRequest(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            contact_request.save()
            messages.success(request, 'Your message has been sent. We will contact you soon!')
            return redirect('print_shop:contact')
    else:
        form = ContactForm()
    
    return render(request, 'print_shop/contact.html', {'form': form})

def portfolio(request):
    return render(request, 'print_shop/portfolio.html')

def printing(request):
    printing_services = Service.objects.filter(slug__contains='print').order_by('order')
    return render(request, 'print_shop/printing.html', {'services': printing_services})

def mailing(request):
    mailing_services = Service.objects.filter(slug__contains='mail').order_by('order')
    return render(request, 'print_shop/mailing.html', {'services': mailing_services})

def marketing(request):
    marketing_services = Service.objects.filter(slug__contains='market').order_by('order')
    return render(request, 'print_shop/marketing.html', {'services': marketing_services})
