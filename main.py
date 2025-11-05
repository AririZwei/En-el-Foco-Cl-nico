# main.py

def define_env(env):
    "Hook para definir macros y variables"

    @env.macro
    def get_page_count(nav_items):
        """
        Una función recursiva para contar todas las páginas en la navegación,
        excluyendo los archivos 'index.md'.
        """
        count = 0
        for item in nav_items:
            if item.is_section:
                # Si es una sección (ej. "Oncología"),
                # llama a esta misma función para contar a sus hijos
                count += get_page_count(item.children)
            elif item.is_page and not item.is_index:
                # Si es una página Y NO es un 'index.md', súmala
                count += 1
        return count