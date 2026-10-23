# R060DIN

## Descrição

Definições da Integração

---

## Resumo

- Campos: 51
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos da Empresa |
| EvNoDi | Number(004,0) | Sim | Evento das Horas Normais Diurnas |
| EvNoNo | Number(004,0) | Sim | Evento das Horas Normais Noturnas |
| GerAdm | String(001) | Sim | Gerar Eventos p/ Colaboradores Admitidos no Período |
| GerDem | String(001) | Sim | Gerar Eventos p/ Colaboradores Demitidos no Período |
| SepDsr | String(001) | Sim | Separar DSR dos Colaboradores Mensalistas |
| RegPrS | Number(003,0) | Sim | Regra da Primeira Semana da Geração de Eventos |
| RegGer | Number(003,0) | Sim | Regra do Período de Geração |
| RegPrj | Number(003,0) | Sim | Regra do Período de Projeção |
| RegFin | Number(003,0) | Sim | Regra do Cálculo Final da Geração de Eventos |
| ArqMod | String(011) | Sim | Nome do Modelo do Relatório a Ser Emitido Após Geração de Eventos |
| EvDsrD | Number(004,0) | Sim | Código do Evento p/ Pagto DSR Diurno |
| EvDsrN | Number(004,0) | Sim | Código do Evento p/ Pagto DSR Noturno |
| EvPerD | Number(004,0) | Sim | Código do Evento p/ Perda DSR Diurno |
| EvPerN | Number(004,0) | Sim | Código do Evento p/ Perda DSR Noturno |
| CalMis | String(001) | Sim | Tipo de Cálculo do DSR Misto |
| ConNot | String(001) | Sim | Converter Horas Noturnas p/ Cálculo do DSR |
| GerCEs | String(001) | Sim | Calcular o DSR Conforme os Dias de DSR da Escala |
| PagUSe | String(001) | Sim | Pagar o DSR da Última Semana |
| FerCom | String(001) | Sim | Pagar Feriado em Dia Compensado |
| FerFol | String(001) | Sim | Pagar Feriado em Dia de Folga |
| ConFal | Number(001,0) | Sim | Considerar Faltas para Perda do DSR no Feriado |
| HorFer | String(001) | Sim | Considerar as Horas de Feriado |
| SitFFe | Number(003,0) | Sim | Código da Situação de Falta Férias a Ser Gerado no Afastamento |
| LimHor | Number(010,0) | Sim | Limite de Horas da Situação de Falta Férias |
| LimOco | Number(002,0) | Sim | Limite de Ocorrências da Situação de Falta Férias |
| RecMeA | String(001) | Sim | Utiliza Recálculo de Meses Anteriores |
| ModRec | String(011) | Sim | Nome do Modelo do Relatório a Ser Emitido Após Recálculo de Eventos |
| EvEDsr | Number(004,0) | Sim | Evento Reflexo das Horas Extra sobre DSR |
| GerDif | String(001) | Sim | Gerar Diferenças Automaticamente no Recálculo da Integração |
| IntPen | String(001) | Sim | Integrar com pendências de acerto |
| IntVer | String(001) | Sim | Integrar com dias não verificados |
| DsrSeg | String(001) | Sim | Descontar DSRs seguidos em escalas de revezamento |
| SomRev | String(001) | Sim | Descontar somente de escalas de revezamento |
| EMDsrD | Number(004,0) | Sim | Evento pagamento multa DSR diurno |
| EMDsrN | Number(004,0) | Sim | Evento pagamento multa DSR noturno |
| EvHEBH | Number(004,0) | Sim | Evento Horas Extras Banco de Horas |
| EvHCBH | Number(004,0) | Sim | Evento Horas Compensadas Banco de Horas |
| GerHRe | String(001) | Sim | Gerar Horas Normais Realizadas |
| EvAteD | Number(004,0) | Sim | Evento Atest Sem Inc.INSS Diurno |
| EvAteN | Number(004,0) | Sim | Evento Atest Sem Inc.INSS Noturno |
| EvFToD | Number(004,0) | Sim | Evento faltas totais diurno |
| EvFToN | Number(004,0) | Sim | Evento faltas totais noturno |
| EvFPaD | Number(004,0) | Sim | Evento faltas parciais diurno |
| EvFPaN | Number(004,0) | Sim | Evento faltas parciais noturno |
| EpFDsD | Number(004,0) | Sim | Evento faltas perda DSR diurno eSocial |
| EpFDsN | Number(004,0) | Sim | Evento faltas perda DSR noturno eSocial |
| EpADsD | Number(004,0) | Sim | Evento atrasos perda DSR diurno eSocial |
| EpADsN | Number(004,0) | Sim | Evento atrasos perda DSR noturno eSocial |
| EvRfEm | Number(004,0) | Sim | Evento Total Refeição Empresa |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R060DIN_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R060DIN_001

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

