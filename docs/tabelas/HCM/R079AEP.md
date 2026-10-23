# R079AEP

## Descrição

Avaliação de Excelência - Pesos

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| PesAv1 | Number(002,0) | Sim | Peso da Autoavaliação |
| PesAv2 | Number(002,0) | Sim | Peso da Avaliação dos Superiores |
| PesAv3 | Number(002,0) | Sim | Peso da Avaliação dos Subordinados |
| PesAv4 | Number(002,0) | Sim | Peso da Avaliação dos Cargos Pares |
| PesAv5 | Number(002,0) | Sim | Peso da Avaliação dos Clientes |
| PesAv6 | Number(002,0) | Sim | Peso da Avaliação dos Fornecedores |
| PesAv7 | Number(002,0) | Sim | Peso da Avaliação dos Instrutores |
| PesAv8 | Number(002,0) | Sim | Peso da avaliação de consenso |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R079AEP_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

