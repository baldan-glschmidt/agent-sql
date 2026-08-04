# E076LMC

## Descrição

Cadastros - Marcas - Ligação Marca X Condição Pagamento

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMar | String(010) | Não | Código da Marca/Etiqueta |
| EmpCpg | Number(004,0) | Não | Código da empresa da Condição de Pagamento |
| CodCpg | String(006) | Não | Código da condição de pagamento |
| SitLmc | String(001) | Não | Situação da ligação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da útima altualização do cadastro |

---

## Chave Primária

- CodMar
- EmpCpg
- CodCpg

---

## Índices

### E076LMCIndice1

**Tipo:** Não unico

Campos:
- EmpCpg
- CodCpg

---

## Relacionamentos

### IR_E076LMC_000

**Tabela:** E076MAR

| Origem | Destino |
|--------|---------|
| CodMar | CodMar |

### IR_E076LMC_002

**Tabela:** E028CPG

| Origem | Destino |
|--------|---------|
| EmpCpg | CodEmp |
| CodCpg | CodCpg |

