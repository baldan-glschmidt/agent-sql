# R134DTU

## Descrição

Turmas - Definição

---

## Resumo

- Campos: 51
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| DatIni | Date | Sim | Data Início do Curso |
| DatFim | Date | Sim | Data de Término |
| QtdAul | Number(003,0) | Sim | Quantidade de Aulas |
| TipDur | Number(001,0) | Sim | Tipo de Duração |
| TemDur | Number(003,0) | Sim | Tempo de Duração |
| CarHor | Number(010,0) | Sim | Carga Horária |
| QtdVag | Number(006,0) | Sim | Quantidade de Vagas |
| TipRea | Number(003,0) | Sim | Tipo de Realização |
| CodFes | Number(008,0) | Sim | Código da Entidade |
| MedCua | Number(005,2) | Sim | Média Mínima do Curso |
| FreCua | Number(005,2) | Sim | % de Frequência Mínima do Curso |
| TipCnf | Number(001,0) | Sim | Tipo de Definição |
| SitCua | Number(001,0) | Sim | Tipo da Situação |
| CodUsu | Number(010,0) | Sim | Identificação do Coordenador da Turma |
| FasCua | String(003) | Sim | Fase do Curso de Aperfeiçoamento |
| RegExc | Number(003,0) | Sim | Regra para Exclusão de Participante da Turma |
| RegSub | Number(003,0) | Sim | Regra para Substituição de Participante da Turma |
| RegTrf | Number(003,0) | Sim | Regra para Transferência de Participante da Turma |
| DvgWEB | String(001) | Sim | Divulga a Turma na WEB |
| CodTst | String(005) | Sim | Código do questionário da  avaliação de eficácia |
| IniEfi | Number(003,0) | Sim | Prazo em dias, para começar a avaliação de eficácia |
| PraAva | Number(003,0) | Sim | Prazo em dias, para ocorrer a avaliação de eficácia |
| AvRWeb | String(001) | Sim | Efetuar Avaliação de Reação via WEB |
| PraARe | Number(003,0) | Sim | Prazo em dias, para ocorrer a avaliação de reação |
| SitART | Number(001,0) | Sim | Situação da Avaliação de Reação da Turma |
| CriRep | Number(001,0) | Sim | Define se a reprovação será por média ou frequencia quando ambas estiverem abaixo do mínimo |
| AltTur | String(001) | Sim | Usuário alterou o cadastro da turma |
| AltIns | String(001) | Sim | Usuário alterou os instrutores da turma |
| AltPar | String(001) | Sim | Usuário alterou os participantes da turma |
| DatCan | Date | Sim | Data Cancelamento do Curso |
| CodMoc | Number(003,0) | Sim | Código do Motivo |
| RegInc | Number(003,0) | Sim | Regra para Inclusão de Participante da Turma |
| RegCpl | Number(003,0) | Sim | Regra para complementar a avaliação do participante |
| CodCla | Number(003,0) | Sim | Definição da classificação das turmas |
| DatLim | Date | Sim | Prazo para inscrições de participantes na turma |
| VinIde | String(001) | Sim | Vincular identificadores da avaliação de reação aos participantes automaticamente |
| AvrAno | String(001) | Sim | Permitir transformar uma avaliação de reação identificada em anônima |
| ConFre | Number(001,0) | Sim | Define a forma de controlar a frequência do participante |
| DesCon | String(8001) | Sim | Descrição do Conteúdo |
| DesObu | String(2000) | Sim | Descrição do Objetivo |
| MetCua | String(1000) | Sim | Metodologia Curso |
| PubAlv | String(400) | Sim | Público Alvo |
| EmpRsp | Number(004,0) | Sim | Código da Empresa do Responsável |
| TipRsp | Number(001,0) | Sim | Tipo de Colaborador Responsável |
| CadRsp | Number(009,0) | Sim | Cadastro do Responsável |
| EmpTLT | Number(004,0) | Sim | Código da Empresa de Origem dos Itens de TLT |
| OrgTLT | Number(004,0) | Sim | Código da Tabela de Organograma de Origem dos Itens de TLT |
| LocTLT | Number(009,0) | Sim | Código do Local de Origem dos Itens de TLT |
| TipTre | Number(001,0) | Sim | Tipo do treinamento/capacitação |

---

## Chave Primária

- CodCua
- TmaCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134DTU_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R134DTU_009

**Tabela:** R140REA

| Origem | Destino |
|--------|---------|
| TipRea | TipRea |

