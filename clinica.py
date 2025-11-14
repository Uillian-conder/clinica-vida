"""
Sistema de Cadastro de Pacientes - Clínica Vida+
Desenvolvido para o Projeto Integrado
"""

def exibir_menu():
    """Exibe o menu principal do sistema"""
    print("\n" + "="*40)
    print("   SISTEMA CLÍNICA VIDA+")
    print("="*40)
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Controle de acesso do paciente")
    print("6. Sair")
    print("="*40)



# ==========================================
#       MÓDULO DE CONTROLE DE ACESSO
# ==========================================
def verificar_atendimento(tipo, A, B, C, D):
    """Verifica se o paciente pode ser atendido conforme as regras"""

    # CONSULTA NORMAL
    if tipo == "normal":
        return (A and B and C) or (B and C and D)

    # EMERGÊNCIA
    elif tipo == "emergencia":
        return C and (B or D)

    else:
        print("❌ Tipo de atendimento inválido!")
        return False


def controle_de_acesso():
    """Executa a lógica de controle de acesso"""
    print("\n--- CONTROLE DE ACESSO ---")

    tipo = input("Tipo de atendimento (normal/emergencia): ").strip().lower()

    print("\nResponda com S para sim e N para não:")

    A = input("Paciente tem agendamento? (S/N): ").strip().upper() == "S"
    B = input("Documentos estão em dia (RG/CPF)? (S/N): ").strip().upper() == "S"
    C = input("Há médico disponível? (S/N): ").strip().upper() == "S"
    D = input("Pagamentos anteriores estão em dia? (S/N): ").strip().upper() == "S"

    pode = verificar_atendimento(tipo, A, B, C, D)

    if pode:
        print("\n✅ ATENDIMENTO LIBERADO")
    else:
        print("\n❌ ATENDIMENTO NEGADO")



# ==========================================
#       MÓDULO DE PACIENTES
# ==========================================

def cadastrar_paciente(pacientes):
    """Cadastra um novo paciente no sistema"""
    try:
        print("\n--- CADASTRO DE PACIENTE ---")
        nome = input("Nome do paciente: ").strip()
        
        if not nome:
            print("❌ Erro: Nome não pode estar vazio!")
            return
        
        idade_str = input("Idade: ").strip()
        
        # Validação da idade
        try:
            idade = int(idade_str)
            if idade < 0 or idade > 150:
                print("❌ Erro: Idade inválida!")
                return
        except ValueError:
            print("❌ Erro: Digite um número válido para idade!")
            return
        
        telefone = input("Telefone: ").strip()
        
        if not telefone:
            print("❌ Erro: Telefone não pode estar vazio!")
            return
        
        # Cria dicionário com dados do paciente
        paciente = {
            'nome': nome,
            'idade': idade,
            'telefone': telefone
        }
        
        pacientes.append(paciente)
        print("✅ Paciente cadastrado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao cadastrar paciente: {e}")


def ver_estatisticas(pacientes):
    """Exibe estatísticas dos pacientes cadastrados"""
    if not pacientes:
        print("\n⚠️  Nenhum paciente cadastrado ainda!")
        return
    
    print("\n--- ESTATÍSTICAS DA CLÍNICA ---")
    
    total = len(pacientes)
    print(f"📊 Total de pacientes: {total}")
    
    idades = [p['idade'] for p in pacientes]
    idade_media = sum(idades) / len(idades)
    print(f"📊 Idade média: {idade_media:.1f} anos")
    
    paciente_mais_novo = min(pacientes, key=lambda p: p['idade'])
    print(f"👶 Paciente mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)")
    
    paciente_mais_velho = max(pacientes, key=lambda p: p['idade'])
    print(f"👴 Paciente mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)")


def buscar_paciente(pacientes):
    """Busca um paciente pelo nome"""
    if not pacientes:
        print("\n⚠️  Nenhum paciente cadastrado ainda!")
        return
    
    print("\n--- BUSCAR PACIENTE ---")
    nome_busca = input("Digite o nome do paciente: ").strip().lower()
    
    encontrados = [p for p in pacientes if nome_busca in p['nome'].lower()]
    
    if encontrados:
        print(f"\n✅ {len(encontrados)} paciente(s) encontrado(s):")
        for p in encontrados:
            print(f"\n  Nome: {p['nome']}")
            print(f"  Idade: {p['idade']} anos")
            print(f"  Telefone: {p['telefone']}")
    else:
        print("❌ Nenhum paciente encontrado com esse nome!")


def listar_pacientes(pacientes):
    """Lista todos os pacientes cadastrados"""
    if not pacientes:
        print("\n⚠️  Nenhum paciente cadastrado ainda!")
        return
    
    print("\n--- LISTA DE PACIENTES ---")
    print(f"Total: {len(pacientes)} paciente(s)\n")
    
    for i, p in enumerate(pacientes, 1):
        print(f"{i}. {p['nome']}")
        print(f"   Idade: {p['idade']} anos")
        print(f"   Telefone: {p['telefone']}")
        print()



# ==========================================
#                 MAIN
# ==========================================

def main():
    pacientes = []
    
    print("\n🏥 Bem-vindo ao Sistema da Clínica Vida+!")
    
    while True:
        exibir_menu()
        
        try:
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == '1':
                cadastrar_paciente(pacientes)

            elif opcao == '2':
                ver_estatisticas(pacientes)

            elif opcao == '3':
                buscar_paciente(pacientes)

            elif opcao == '4':
                listar_pacientes(pacientes)

            elif opcao == '5':
                controle_de_acesso()

            elif opcao == '6':
                print("\n👋 Encerrando sistema. Até logo!")
                break

            else:
                print("❌ Opção inválida! Digite um número de 1 a 6.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Sistema interrompido pelo usuário. Até logo!")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")


if __name__ == "__main__":
    main()
