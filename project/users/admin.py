from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils import timezone
from .models import Profile, EmailVerification
from AI_assistent.models import Recipes


@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    list_display = [
        'id',
        'username',
        'email',
        'gender',
        'country',
        'birth_date',
        'date_joined',
        'is_active',
        'is_staff'
    ]

    list_display_links = ['id', 'username']

    list_filter = [
        'gender',
        'country',
        'is_active',
        'is_staff',
        'date_joined'
    ]

    search_fields = [
        'username',
        'email',
        'first_name',
        'last_name'
    ]

    ordering = ['-date_joined']

    fieldsets = (
        ('Account Information', {
            'fields': ('username', 'email', 'password')
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'gender', 'birth_date', 'country')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        ('Create New User', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2',
                       'gender', 'birth_date', 'country'),
        }),
    )

    readonly_fields = ['last_login', 'date_joined']

    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, f"{queryset.count()} users were successfully activated.")

    make_active.short_description = "Activate selected users"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f"{queryset.count()} users were successfully deactivated.")

    make_inactive.short_description = "Deactivate selected users"


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'code',
        'created_at',
        'expires_at',
        'status',
        'is_used'
    ]

    list_display_links = ['id', 'code']

    list_filter = [
        'is_used',
        'created_at',
        'expires_at'
    ]

    search_fields = [
        'user__username',
        'user__email',
        'code'
    ]

    readonly_fields = ['created_at', 'expires_at']

    fieldsets = (
        ('Verification Information', {
            'fields': ('user', 'code')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'expires_at')
        }),
        ('Status', {
            'fields': ('is_used',)
        }),
    )

    def status(self, obj):
        if obj.is_used:
            return "Used"
        elif obj.is_expired():
            return "Expired"
        else:
            return "Active"

    status.short_description = "Status"

    actions = ['mark_as_used', 'delete_expired']

    def mark_as_used(self, request, queryset):
        queryset.update(is_used=True)
        self.message_user(request, f"{queryset.count()} verifications were marked as used.")

    mark_as_used.short_description = "Mark as used"

    def delete_expired(self, request, queryset):
        expired = queryset.filter(expires_at__lt=timezone.now())
        count = expired.count()
        expired.delete()
        self.message_user(request, f"{count} expired verifications were deleted.")

    delete_expired.short_description = "Delete expired"


admin.site.site_header = "SmartRecipe Administration"
admin.site.site_title = "SmartRecipe Admin"
admin.site.index_title = "Welcome to SmartRecipe Admin Panel"
