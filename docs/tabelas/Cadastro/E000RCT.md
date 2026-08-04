# E000RCT

## Descrição

Tabelas - Integrações - Receituário Agronômico

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodEtp | Number(004,0) | Sim | Código da espécie/cultura |
| CodDpp | Number(004,0) | Sim | Código da praga/problema |
| CodDia | Number(009,0) | Sim | Código do diagnóstico |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| SigUfs | String(002) | Sim | UF |

---

## Chave Primária

- SeqInt

---

## Índices

### E000RCTIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodEtp
- CodDpp
- CodDia
- CodPro
- CodDer
- SigUfs

---

## Relacionamentos

Nenhum relacionamento cadastrado.
