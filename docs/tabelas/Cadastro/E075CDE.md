# E075CDE

## Descrição

Cadastros - Produtos - Características p/ Derivação

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da Derivação do Produto |
| CodCte | String(003) | Não | Código da característica do produto |
| SeqCcp | Number(009,0) | Não | Número da sequência da característica válido para o produto |
| DesLiv | String(250) | Sim | Descrição Livre da característica válido para o produto |
| ObsLiv | String(240) | Sim | Observação livre da característica de produto/derivação |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodCte
- SeqCcp

---

## Índices

### E075CDEIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodCte

---

## Relacionamentos

### IR_E075CDE_003

**Tabela:** E010CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCte | CodCte |

