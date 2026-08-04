# E900ETQ

## Descrição

Etiquetas originadas da plataforma Senior X

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeApt | Number(009,0) | Não | Identificador único do apontamento |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodEtq | String(032) | Sim | Código da etiqueta |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| QtdEtq | Number(014,5) | Não | Quantidade da etiqueta |
| TipEtq | String(001) | Não | Tipo da etiqueta |
| SitEtq | String(001) | Não | Situação da etiqueta |
| Aux001 | String(050) | Sim | Auxiliar 001 |
| Aux002 | String(050) | Sim | Auxiliar 002 |

---

## Chave Primária

- IdeUni

---

## Índices

### E900ETQIndice1

**Tipo:** Não unico

Campos:
- IdeApt

### E900ETQIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer

---

## Relacionamentos

### IR_E900ETQ_001

**Tabela:** E900APT

| Origem | Destino |
|--------|---------|
| IdeApt | IdeUni |

### IR_E900ETQ_005

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

