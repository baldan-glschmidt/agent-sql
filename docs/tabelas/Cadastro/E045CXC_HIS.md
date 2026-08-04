# E045CXC_HIS

## Descrição

Tabelas - Histórico - Plano Contábil - Relacionamento Contas X Centro de Custos Liberados

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodMpc | Number(004,0) | Não | Código do modelo de plano |
| CtaRed | Number(007,0) | Não | Conta contábil reduzida |
| CodCcu | String(009) | Não | Código do centro de custos liberado |
| CriCxc | Number(001,0) | Não | Critério para relacionamento (1 = Só ele, 2 = Todas subordinadas a ele) |
| ObsCxc | String(250) | Sim | Observação do relacionamento |
| SitCxc | String(001) | Não | Situação do relacionamento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do registro |
| HorAtu | Number(005,0) | Sim | Hora da última atualização do registro |

---

## Chave Primária

- CodEmp
- CodMpc
- CtaRed
- CodCcu

---

## Índices

### E045CXC_HISIndice1

**Tipo:** Não unico

Campos:
- CodMpc

---

## Relacionamentos

### IR_E045CXC_HIS_001

**Tabela:** E043MPC

| Origem | Destino |
|--------|---------|
| CodMpc | CodMpc |

### IR_E045CXC_HIS_002

**Tabela:** E045PLA_HIS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMpc | CodMpc |
| CtaRed | CtaRed |

