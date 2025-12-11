/**
 * Validación simplificada del formulario
 */

document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('formularioMateria');
    
    if (formulario) {
        // Validación en tiempo real para campos obligatorios
        const camposObligatorios = formulario.querySelectorAll('[required]');
        
        camposObligatorios.forEach(campo => {
            campo.addEventListener('blur', function() {
                validarCampo(this);
            });
            
            campo.addEventListener('input', function() {
                if (this.value.trim()) {
                    this.classList.remove('is-invalid');
                    this.classList.add('is-valid');
                }
            });
        });
        
        // Validación del formulario al enviar
        formulario.addEventListener('submit', function(event) {
            let esValido = true;
            
            camposObligatorios.forEach(campo => {
                if (!validarCampo(campo)) {
                    esValido = false;
                }
            });
            
            if (!esValido) {
                event.preventDefault();
                mostrarMensaje('Por favor, completa todos los campos requeridos correctamente.', 'danger');
            }
        });
        
        // Validar código único (simplificado)
        const codigoInput = document.getElementById('id_codigo');
        if (codigoInput) {
            codigoInput.addEventListener('blur', function() {
                const codigo = this.value.trim();
                if (codigo.length > 0 && codigo.length < 3) {
                    this.classList.add('is-invalid');
                    this.classList.remove('is-valid');
                }
            });
        }
    }
    
    // Funciones auxiliares
    function validarCampo(campo) {
        const valor = campo.value.trim();
        
        if (!valor) {
            campo.classList.add('is-invalid');
            campo.classList.remove('is-valid');
            return false;
        }
        
        // Validaciones específicas
        if (campo.type === 'number') {
            const min = campo.min ? parseInt(campo.min) : -Infinity;
            const max = campo.max ? parseInt(campo.max) : Infinity;
            const num = parseInt(valor);
            
            if (isNaN(num) || num < min || num > max) {
                campo.classList.add('is-invalid');
                campo.classList.remove('is-valid');
                return false;
            }
        }
        
        campo.classList.remove('is-invalid');
        campo.classList.add('is-valid');
        return true;
    }
    
    function mostrarMensaje(texto, tipo) {
        // Crear alerta
        const alerta = document.createElement('div');
        alerta.className = `alert alert-${tipo} alert-dismissible fade show`;
        alerta.innerHTML = `
            ${texto}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        // Insertar al inicio del formulario
        formulario.parentNode.insertBefore(alerta, formulario);
        
        // Auto-eliminar después de 5 segundos
        setTimeout(() => {
            if (alerta.parentNode) {
                alerta.remove();
            }
        }, 5000);
    }
});