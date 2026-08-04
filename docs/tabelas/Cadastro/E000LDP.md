# E000LDP

## Descrição

Tabelas - Integrações - Itens Log de Integração Receituário Agronômico

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeLog | Number(009,0) | Não | Identificador de Log |
| CodIde | String(014) | Não | Código ID do sistema parceiro |
| NomTab | String(032) | Sim | Tabela no Sistema Senior |
| NomCam | String(400) | Sim | Nomes dos campos chave na tabela |
| CodIpa | String(400) | Sim | Valores dos campos na tabela |
| CodEmp | Number(004,0) | Sim | Código da empresa |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação do produto |
| DesPro | String(100) | Sim | Descrição usual do produto |
| SitPro | String(001) | Sim | Situação do registro (A-Ativo ou I-Inativo) |
| UndApl | String(100) | Sim | Código da unidade de aplicação |

---

## Chave Primária

- IdeUni

---

## Índices

### E000LDPIndice1

**Tipo:** Não unico

Campos:
- CodIde

### E000LDPIndice2

**Tipo:** Não unico

Campos:
- NomTab

---

## Relacionamentos

Nenhum relacionamento cadastrado.
