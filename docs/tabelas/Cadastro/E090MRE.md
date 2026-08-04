# E090MRE

## Descrição

Cadastros - Representantes - Definições de Representante X Marca

---

## Resumo

- Campos: 13
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRep | Number(009,0) | Não | Código do representante |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodMar | String(010) | Não | Código da Marca/Etiqueta |
| CodTpr | String(004) | Sim | Código da tabela de preço padrão para o representante |
| CodCpg | String(006) | Sim | Código da condição de pagamento padrão para o representante |
| CodLip | String(005) | Sim | Código da lista de preço padrão para o representante |
| PerCom | Number(005,2) | Sim | Percentual de comissão padrão do representante para a marca |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodRep
- CodEmp
- CodMar

---

## Índices

### E090MREIndice1

**Tipo:** Não unico

Campos:
- CodMar

---

## Relacionamentos

### IR_E090MRE_000

**Tabela:** E090REP

| Origem | Destino |
|--------|---------|
| CodRep | CodRep |

### IR_E090MRE_002

**Tabela:** E076MAR

| Origem | Destino |
|--------|---------|
| CodMar | CodMar |

