from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection
from django.db.utils import OperationalError
import time

class Command(BaseCommand):
    help = 'Runs migrations and seeds initial data if needed'

    def handle(self, *args, **options):
        # Wait for database to be available
        self.stdout.write('Waiting for database...')
        db_conn = None
        for i in range(30):  # try for 30 seconds
            try:
                connection.ensure_connection()
                db_conn = True
                break
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        
        if db_conn:
            self.stdout.write(self.style.SUCCESS('Database available!'))
            
            # Run migrations
            self.stdout.write('Running migrations...')
            call_command('migrate')
            self.stdout.write(self.style.SUCCESS('Migrations complete!'))
            
            # Collect static files
            self.stdout.write('Collecting static files...')
            call_command('collectstatic', '--noinput')
            self.stdout.write(self.style.SUCCESS('Static files collected!'))
            
            # Create sample data if needed
            from print_shop.models import Service, Testimonial, Post
            
            if not Service.objects.exists():
                self.stdout.write('Creating sample services...')
                Service.objects.create(
                    title='Printing Services',
                    description='High-quality printing services for all your business needs.',
                    slug='printing-services',
                    order=1
                )
                Service.objects.create(
                    title='Mailing Services',
                    description='Direct mail services to reach your target audience.',
                    slug='mailing-services',
                    order=2
                )
                Service.objects.create(
                    title='Marketing Services',
                    description='Marketing solutions to help grow your business.',
                    slug='marketing-services',
                    order=3
                )
                self.stdout.write(self.style.SUCCESS('Sample services created!'))
            
            if not Testimonial.objects.exists():
                self.stdout.write('Creating sample testimonials...')
                Testimonial.objects.create(
                    name='John Smith',
                    quote='TEKS Services provided excellent printing services for our business. Highly recommended!',
                    active=True
                )
                Testimonial.objects.create(
                    name='Jane Doe',
                    quote='The quality of their work is outstanding. We\'ll definitely use their services again.',
                    active=True
                )
                self.stdout.write(self.style.SUCCESS('Sample testimonials created!'))
            
            if not Post.objects.exists():
                self.stdout.write('Creating sample blog posts...')
                from django.utils import timezone
                
                Post.objects.create(
                    title='Things we print',
                    content='At TEKS Services, we offer a wide range of printing services to meet all your business needs.',
                    published_date=timezone.now(),
                    slug='things-we-print'
                )
                Post.objects.create(
                    title='Table-Top Banners with an X-Frame',
                    content='Table-top banners with an X-frame are perfect for trade shows, retail displays, and events.',
                    published_date=timezone.now() - timezone.timedelta(days=30),
                    slug='table-top-banners'
                )
                Post.objects.create(
                    title='Self Mailers & Tabbing Rules',
                    content='The USPS has specific requirements for self-mailers to ensure they can be processed through automated equipment.',
                    published_date=timezone.now() - timezone.timedelta(days=60),
                    slug='self-mailers-tabbing-rules'
                )
                self.stdout.write(self.style.SUCCESS('Sample blog posts created!'))
            
            self.stdout.write(self.style.SUCCESS('Setup complete!'))
        else:
            self.stdout.write(self.style.ERROR('Database unavailable!'))
