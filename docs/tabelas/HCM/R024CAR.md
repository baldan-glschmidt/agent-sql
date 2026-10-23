# R024CAR

## Descrição

Cargos

---

## Resumo

- Campos: 33
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| TitRed | String(030) | Sim | Título Reduzido do Cargo |
| TitCar | String(100) | Sim | Título do  Cargo |
| CarAlf | String(010) | Sim | Código Alfa do Cargo |
| CodHie | Number(003,0) | Sim | Código da Hierarquia |
| SupIme | String(024) | Sim | Código Superior Imediato |
| SupIm2 | String(024) | Sim | Código Superior Imediato II |
| CodCbo | String(005) | Sim | Cbo do Cargo |
| HorMes | Number(010,0) | Sim | Horas Mês Contratuais |
| SisCar | Number(002,0) | Sim | Tipo do Sistema do Cargo |
| NatDes | Number(003,0) | Sim | Natureza Despesa |
| DesSum | String(5000) | Sim | Descrição Sumária do Cargo |
| DatCri | Date | Sim | Data de Criação do Cargo |
| DatExt | Date | Sim | Data de Extinção do Cargo |
| GraCpx | String(001) | Sim | Grau de Complexidade do Cargo |
| NivCar | Number(001,0) | Sim | Nível do Cargo |
| PerFnc | Number(009,5) | Sim | % Adicional de Função |
| NomArq | String(250) | Sim | Arquivo |
| CodSig | String(007) | Sim | Sigla Conselho Profissional |
| CodCb2 | String(006) | Sim | Cbo 2002 do Cargo |
| CarCom | String(001) | Sim | Define se o Cargo é de comando - Utilizado no PPP |
| CarMap | String(015) | Sim | Código do cargo no sistema MAP |
| AreAtu | Number(003,0) | Sim | Código da área de atuação |
| ArqCri | String(250) | Sim | Arquivo de criação do cargo |
| ArqExt | String(250) | Sim | Arquivo de extinção do cargo |
| CodHwf | Number(003,0) | Sim | Código da Hierarquia do Workflow |
| OclObr | String(001) | Sim | Define obrigatoriedade do campo Órgão de Classe |
| CNHObr | String(001) | Sim | Define a obrigatoriedade do campo CNH |
| TipMot | Number(001,0) | Sim | Tipo do motorista |
| USU_ParPro | String(001) | Sim | Indicar se o cargo participa do Probia |
| USU_NivCar | String(002) | Sim | Nível de Maturidade do Cargo |
| USU_ConCot | String(001) | Sim | Considera para Cota (Menor Aprendiz) |

---

## Chave Primária

- EstCar
- CodCar

---

## Índices

### R024CARIndice2

**Tipo:** Não unico

Campos:
- EstCar
- TitRed

---

## Relacionamentos

### IR_R024CAR_000

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

