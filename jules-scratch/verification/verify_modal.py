import os
from playwright.sync_api import sync_playwright, expect, Page

def verify_modal_opens(page: Page):
    """
    This test verifies that clicking a tool card opens the file upload modal.
    """
    # 1. Arrange: Go to the index.html file served by the HTTP server.
    page.goto('http://localhost:8000/index.html')

    # 2. Act: Find the "PDF to Word" tool card and dispatch a click event.
    tool_card = page.locator('[data-tool="pdf-to-word"]')
    tool_card.dispatch_event('click')

    # 3. Assert: Confirm the modal is visible.
    modal = page.locator("#toolModal")
    expect(modal).to_be_visible()

    # 4. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    verify_modal_opens(page)
    browser.close()
