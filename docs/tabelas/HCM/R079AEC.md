# R079AEC

## Descrição

Avaliação de Conhecimentos - Pesos

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
| PesAv1 | Number(002,0) | Sim | Peso da autoavaliação |
| PesAv2 | Number(002,0) | Sim | Peso da Avaliação dos superiores |
| PesAv3 | Number(002,0) | Sim | Peso da avaliação dos subordinados |
| PesAv4 | Number(002,0) | Sim | Peso da avaliação dos cargos pares |
| PesAv5 | Number(002,0) | Sim | Peso da avaliação dos clientes |
| PesAv6 | Number(002,0) | Sim | Peso da avaliação dos fornecedores |
| PesAv7 | Number(002,0) | Sim | Peso da avaliação dos instrutores |
| PesAv8 | Number(002,0) | Sim | Peso da avaliação de consenso |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R079AEC_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

