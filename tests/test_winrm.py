import winrm

try:
    # Intentar con diferentes opciones
    session = winrm.Session(
        '192.168.0.36',
        auth=('administrador', 'Olitec0'),
        transport='basic',
        server_cert_validation='ignore'
    )
    
    # Comando simple
    result = session.run_cmd('ipconfig', ['/all'])
    print("✅ CONEXIÓN EXITOSA")
    print("Exit code:", result.status_code)
    print("Output:", result.std_out.decode('utf-8'))
    
except Exception as e:
    print("❌ ERROR:", str(e))
    
    # Probar alternativa con protocolo directo
    print("\n=== INTENTANDO MÉTODO ALTERNATIVO ===")
    try:
        from winrm.protocol import Protocol
        p = Protocol(
            endpoint='http://192.168.0.36:5985/wsman',
            transport='plaintext',
            username='administrador',
            password='Olitec0',
            server_cert_validation='ignore'
        )
        shell_id = p.open_shell()
        print("✅ Shell abierto exitosamente")
        p.close_shell(shell_id)
    except Exception as e2:
        print("❌ Error alternativo:", str(e2))
