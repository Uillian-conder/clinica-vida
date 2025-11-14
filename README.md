# 🏥 Clínica Vida+  
### Sistema de Cadastro de Pacientes — Projeto Integrado

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Ativo-success)
![Licença](https://img.shields.io/badge/Licença-MIT-green)

---

## 📌 Sobre o Projeto
O **Clínica Vida+** é um sistema desenvolvido para o Projeto Integrado da faculdade, com foco em gerenciar pacientes e organizar o fluxo de atendimento dentro de uma clínica.

O sistema funciona no terminal e permite:

- Cadastro de pacientes  
- Estatísticas automáticas  
- Busca por nome  
- Listagem completa  
- Controle de acesso baseado em regras (A, B, C, D)

---

## 🚀 Funcionalidades

### ✔️ **1. Cadastrar Paciente**
Registra nome, idade e telefone, com validações completas.

### ✔️ **2. Estatísticas**
- Total de pacientes  
- Idade média  
- Paciente mais novo  
- Paciente mais velho  

### ✔️ **3. Buscar Paciente**
Busca parcial, encontrando nomes que contenham o texto digitado.

### ✔️ **4. Listar Pacientes**
Mostra todos os pacientes cadastrados com seus dados.

### ✔️ **5. Controle de Acesso**
Define se o paciente pode ser atendido com base nas regras:

| Regra | Descrição |
|-------|-----------|
| **A** | Tem agendamento |
| **B** | Documentos estão em dia |
| **C** | Há médico disponível |
| **D** | Pagamentos em dia |

Tipos de atendimento:
- Normal
- Emergência

---

## 🧠 Lógica do Controle de Acesso

### 🔹 **Atendimento Normal**
Liberado se:
- (A **e** B **e** C) **ou**
- (B **e** C **e** D)

### 🔹 **Emergência**
Liberado se:
- C **e** (B **ou** D)

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- Entrada e saída via terminal
- Estrutura modular (funções separadas)

---

## 📂 Estrutura do Projeto


---

## ▶️ Como Executar

1. Instale o Python 3.10 ou superior.  
2. Faça o download ou clone o repositório:

```bash
git clone https://github.com/Uillian-conder/clinica-vida

cd clinica-vida

python clinica.py
