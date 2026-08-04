# E088LPC

## Descrição

Tabelas - Certificado de Classificação - Ligação Produto ao Certificado de Classificação

---

## Resumo

- Campos: 6
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| SerCcl | String(003) | Não | Série do certificado de classificação |
| NumCcl | String(015) | Não | Número do certificado de classificação |
| CodPro | String(014) | Não | Código do produto ligado ao certificado |
| CodDer | String(007) | Não | Código da derivação do produto ligado ao certificado |
| CodFil | Number(005,0) | Não | Código da filial |

---

## Chave Primária

- CodEmp
- SerCcl
- NumCcl
- CodPro
- CodDer
- CodFil

---

## Índices

### E088LPCIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro

---

## Relacionamentos

### IR_E088LPC_002

**Tabela:** E088CCL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| SerCcl | SerCcl |
| NumCcl | NumCcl |

### IR_E088LPC_003

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

