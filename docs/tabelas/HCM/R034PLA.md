# R034PLA

## Descrição

Definições de Acesso do Colaborador por Planta

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| CodPlt | Number(005,0) | Não | Código do Site |
| DatAso | Date | Sim | Data Validade do ASO |
| DatTse | Date | Sim | Data Validade Treinamento Segurança |
| BloPlt | String(001) | Sim | Bloquear a pessoa no site |
| Pen063 | Number(001,0) | Sim | Pendência gerada |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
