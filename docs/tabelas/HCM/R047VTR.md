# R047VTR

## Descrição

CIF - Cadastro de Outras Empresas (Vale Transporte)

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCif | Number(003,0) | Não | Código de Integração Financeira |
| CodOem | Number(008,0) | Não | Código da Outra Empresa |

---

## Chave Primária

- CodCif
- CodOem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R047VTR_000

**Tabela:** R047CIF

| Origem | Destino |
|--------|---------|
| CodCif | CodCif |

### IR_R047VTR_001

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

