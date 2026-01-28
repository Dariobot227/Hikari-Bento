from django.contrib import admin
from .models import Reservation, Contact, MenuItem, Category

# Register models without custom admin
admin.site.register(Reservation)
admin.site.register(Contact)

# Inline display for MenuItems inside Category
class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1  # how many empty forms to show
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" />'
        return ""
    image_preview.allow_tags = True
    image_preview.short_description = "Preview"

# Category admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [MenuItemInline]

# MenuItem admin with custom display
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'image_preview']
    list_filter = ['category']
    search_fields = ['name', 'description']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" />'
        return ""
    image_preview.allow_tags = True
    image_preview.short_description = "Preview"
