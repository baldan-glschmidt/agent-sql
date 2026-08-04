# E000SXT

## Descrição

Tabelas - Integrações - Sistema X Tipo de Informação para Integração

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInt | Number(002,0) | Não | Código do sistema integrado |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| IdeInt | Number(009,0) | Não | Código Identificador do tipo de informação |
| UltNum | Number(009,0) | Sim | Último número de lote gerado. |
| SitReg | String(001) | Sim | Situação da integração do tipo de informação |
| FilCus | String(16958) | Sim | Filtro Customizado para Exportação |

---

## Chave Primária

- CodInt
- CodEmp
- CodFil
- IdeInt

---

## Índices

### E000SXTIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

### IR_E000SXT_002

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

