# R058FAC

## Descrição

Faixa de Acesso dos Coletores

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPrm | Number(005,0) | Não | Código da Permissão |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor da Permissão |
| ModLei | Number(003,0) | Não | Modelo da Leitora |
| IniFai | Number(005,0) | Não | Início da Faixa p/ Marcação de Acesso |
| FimFai | Number(005,0) | Sim | Fim da Faixa p/ Marcação de Acesso |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |

---

## Chave Primária

- CodPrm
- CodPlt
- CodRlg
- ModLei
- IniFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058FAC_000

**Tabela:** R058PRM

| Origem | Destino |
|--------|---------|
| CodPrm | CodPrm |

### IR_R058FAC_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R058FAC_002

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

