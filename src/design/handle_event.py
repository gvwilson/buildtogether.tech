class Actor:
    def __init__(...):
        ...do generic setup...
    def handle_event(self, event):
        if self.has_handler_for(event):
            handler = self.get_handler_for(event)
            handler(event)
        else:
            self.default_action(event)
