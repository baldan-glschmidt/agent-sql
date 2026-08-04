# E000EPT

## Descrição

Tabelas - Integrações - Exceções de Integração de Pagamento de Títulos

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInt | Number(002,0) | Não | Código da Integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SeqEis | Number(009,0) | Não | Sequencia da exceção de integração |
| TipEpt | Number(001,0) | Sim | Tipo de exceção de integração de pagamento de título |
| NumTit | String(015) | Não | Número do título a receber |
| CodTpt | String(003) | Não | Código do tipo de título a receber |

---

## Chave Primária

- CodInt
- CodEmp
- CodFil
- SeqEis

---

## Índices

### E000EPTIndice1

**Tipo:** Unico

Campos:
- CodInt
- CodEmp
- CodFil
- CodTpt
- NumTit
- TipEpt

### E000EPTIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

### IR_E000EPT_000

**Tabela:** E000SIS

| Origem | Destino |
|--------|---------|
| CodInt | CodInt |

### IR_E000EPT_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E000EPT_002

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

