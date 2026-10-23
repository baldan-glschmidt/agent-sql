# R101AVA

## Descrição

Avaliação de Resultado - Identificação

---

## Resumo

- Campos: 31
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| TipAva | Number(002,0) | Não | Sequência do tipo de avaliação |
| SeqAva | Number(002,0) | Não | Sequência da avaliação |
| TpAval | Number(001,0) | Sim | Foco da Avaliação |
| EmpAvl | Number(004,0) | Sim | Empresa do avaliador |
| TipAvl | Number(001,0) | Sim | Tipo do Colaborador Avaliador |
| CadAvl | Number(009,0) | Sim | Cadastro do Avaliador |
| SitAva | Number(001,0) | Sim | Situação da avaliação |
| DatObj | Date | Sim | Data limite para definição de objetivos |
| DatAva | Date | Sim | Data limite para efetuar a avaliação |
| ProObj | Date | Sim | Data de prorrogação de definição |
| ProAva | Date | Sim | Data de prorrogação de avaliação |
| ComChe | String(1500) | Sim | Comentário do avaliador |
| PlaDes | String(2000) | Sim | Plano de desenvolvimento |
| ComEmp | String(1500) | Sim | Comentário do avaliado |
| NumLot | Number(009,0) | Sim | Nr. do lote em que foi gerada a avaliação |
| NotObj | Number(016,4) | Sim | Resultado da avaliação |
| NotCom | Number(016,4) | Sim | Resultado da avaliação de comportamentos |
| NotAva | Number(016,4) | Sim | Resultado geral da avaliação |
| PerObj | Number(005,2) | Sim | % atingido na avaliação dos objetivos |
| PerCom | Number(005,2) | Sim | % atingido na avaliação de comportamentos |
| PerAva | Number(005,2) | Sim | % geral atingido na avaliação |
| ConObj | String(001) | Sim | Identifica se o avaliado tomou conhecimento dos objetivos |
| ConAva | String(001) | Sim | Identifica se o avaliado tomou conhecimento de sua avaliação |
| SitAnt | Number(001,0) | Sim | Situação da avaliação |
| CodUsu | Number(010,0) | Sim | Código do usuário que reabriu a avaliação |
| IdeAva | Number(005,0) | Sim | Identificador da avaliação de competências |
| CodPfa | Number(004,0) | Sim | Indica qual Perfil será utilizado para apresentar a avaliação na WEB |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- TipAva
- SeqAva

---

## Índices

### R101AVAIndice2

**Tipo:** Não unico

Campos:
- EmpAvl
- TipAvl
- CadAvl

---

## Relacionamentos

### IR_R101AVA_004

**Tabela:** R101CTA

| Origem | Destino |
|--------|---------|
| CodCic | CodCic |
| TipAva | TipAva |

