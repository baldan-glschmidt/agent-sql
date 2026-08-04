# E075CPR

## Descrição

Cadastros - Produtos - Características por Produto

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodCte | String(003) | Não | Código da característica do produto |
| SeqCcp | Number(009,0) | Não | Número da sequência da característica válido para o produto |
| DesLiv | String(250) | Sim | Descrição Livre  da característica válido para o produto |
| ObsLiv | String(240) | Sim | Observação livre da característica de produto |
| USU_qtdpes | Number(003,0) | Sim | Quantidades de Pesos |

---

## Chave Primária

- CodEmp
- CodPro
- CodCte
- SeqCcp

---

## Índices

### E075CPRIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodCte

---

## Relacionamentos

### IR_E075CPR_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E075CPR_002

**Tabela:** E010CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCte | CodCte |

