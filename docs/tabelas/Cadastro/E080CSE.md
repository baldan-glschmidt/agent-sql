# E080CSE

## Descrição

Cadastros - Serviços - Características

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodSer | String(014) | Não | Código do produto |
| CodCte | String(003) | Não | Código da característica do produto |
| SeqCcp | Number(004,0) | Sim | Número da sequência da característica válido para o produto |
| DesLiv | String(015) | Sim | Valor da característica válido para o produto |

---

## Chave Primária

- CodEmp
- CodSer
- CodCte

---

## Índices

### E080CSEIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodCte

---

## Relacionamentos

### IR_E080CSE_001

**Tabela:** E080SER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodSer | CodSer |

### IR_E080CSE_002

**Tabela:** E010CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCte | CodCte |

