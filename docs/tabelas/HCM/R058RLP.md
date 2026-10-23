# R058RLP

## Descrição

Coletores da Permissão de Acesso

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPrm | Number(005,0) | Não | Código da Permissão |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor da Permissão |
| ModLei | Number(003,0) | Não | Modelo da Leitora |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| CodFai | Number(003,0) | Sim | Código da Faixa Horária |

---

## Chave Primária

- CodPrm
- CodPlt
- CodRlg
- ModLei
- CodDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058RLP_000

**Tabela:** R058PRM

| Origem | Destino |
|--------|---------|
| CodPrm | CodPrm |

### IR_R058RLP_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R058RLP_002

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

### IR_R058RLP_004

**Tabela:** R058DSP

| Origem | Destino |
|--------|---------|
| CodDsp | CodDsp |

