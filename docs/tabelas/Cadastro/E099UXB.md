# E099UXB

## Descrição

Cadastros - Usuários X Contas Contábeis Liberadas

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Código do Usuário |
| CtaRed | Number(007,0) | Não | Conta contábil reduzida liberada |
| CriUxb | Number(001,0) | Sim | Critério para relacionamento (1=Só ela, 2=Todas subordinadas a ela) |
| ObsUxb | String(250) | Sim | Observação do relacionamento |
| SitUxb | String(001) | Sim | Situação do relacionamento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |

---

## Chave Primária

- CodEmp
- CodUsu
- CtaRed

---

## Índices

### E099UXBIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CtaRed

---

## Relacionamentos

### IR_E099UXB_001

**Tabela:** E099USU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodUsu | CodUsu |

### IR_E099UXB_002

**Tabela:** E045PLA

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CtaRed | CtaRed |

