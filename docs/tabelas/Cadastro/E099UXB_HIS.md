# E099UXB_HIS

## Descrição

Cadastros - Histórico - Usuários X Contas Contábeis Liberadas

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
- Índices: 3
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodMpc | Number(004,0) | Não | Código do modelo de plano |
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
- CodMpc
- CodUsu
- CtaRed

---

## Índices

### E099UXB_HISIndice1

**Tipo:** Não unico

Campos:
- CodMpc

### E099UXB_HISIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodUsu

### E099UXB_HISIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodMpc
- CtaRed

---

## Relacionamentos

### IR_E099UXB_HIS_001

**Tabela:** E043MPC

| Origem | Destino |
|--------|---------|
| CodMpc | CodMpc |

### IR_E099UXB_HIS_002

**Tabela:** E099USU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodUsu | CodUsu |

### IR_E099UXB_HIS_003

**Tabela:** E045PLA_HIS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMpc | CodMpc |
| CtaRed | CtaRed |

