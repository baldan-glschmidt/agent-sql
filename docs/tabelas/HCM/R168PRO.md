# R168PRO

## Descrição

UNISUL - Promoção

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Codigo da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| DatPro | Date | Não | Data Promoção |
| CodMot | Number(003,0) | Sim | Código Motivo |
| EstSal | Number(004,0) | Sim | Código da Estrutura Salarial |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| PerPro | Number(002,0) | Sim | Permanência da Promoção |
| TipPro | Number(002,0) | Sim | Tipo de Promoção |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R168PRO_004

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| CodMot | CodMot |

### IR_R168PRO_005

**Tabela:** R076DES

| Origem | Destino |
|--------|---------|
| EstSal | CodEst |

