# R109FIL

## Descrição

PCMSO - Filial

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodPcm | Number(004,0) | Não | Código de identificação do PCMSO |
| CodFil | Number(006,0) | Não | Código da Filial |

---

## Chave Primária

- NumEmp
- CodPcm
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R109FIL_001

**Tabela:** R109PCM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPcm | CodPcm |

### IR_R109FIL_002

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

