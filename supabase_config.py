from supabase import create_client, Client

SUPABASE_URL = "https://dfbqmskmcowinmgpxsww.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRmYnFtc2ttY293aW5tZ3B4c3d3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDA5MjI1MjUsImV4cCI6MjA1NjQ5ODUyNX0.AhXT0m3OZEUDeL6qIlHmy2fxU6pcTPjjLHBoHeT34Qc"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
