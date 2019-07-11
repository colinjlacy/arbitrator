def create_element(request, responder):
    responder.slots['name'] = request.context.get('name', '')
    responder.slots['element'] = request.context.get('element', '')
    responder.reply(['creating {element} element with name {name}'])
