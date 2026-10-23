# R304ACF

## Descrição

e-Sfinge Online - Atualização do Cargo ou Função

---

## Resumo

- Campos: 29
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipTxt | Number(002,0) | Não | Tipo do texto jurídico |
| NumTxt | String(016) | Não | Número do texto jurídico que atualizou o plano de cargos |
| TipAtu | Number(002,0) | Não | Tipo de atualização |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CarFun | String(016) | Não | Código do cargo ou função atribuído pela unidade |
| DatIni | Date | Não | Data de Início da Vigência do Cargo |
| TipEnv | Number(002,0) | Não | Tipo de envio |
| SeqReg | Number(009,0) | Não | Sequência |
| NomCar | String(100) | Sim | Nome do cargo ou função |
| DatFim | Date | Sim | Data em que o cargo ou função deixou de viger |
| TipCar | Number(002,0) | Sim | Tipo de cargo ou função |
| TipCHr | Number(002,0) | Sim | Tipo da carga horária |
| QtdCHr | Number(007,0) | Sim | Quantidade numérica conforme a carga horária descrita |
| TipAcu | Number(002,0) | Sim | Tipo de cargo para fins de acumulação |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| PidSta | String(030) | Sim | Pid Status |
| CmpAu1 | Date | Sim | Campo Auxiliar 1 |
| CmpAu2 | Date | Sim | Campo Auxiliar 2 |
| CmpAu3 | Number(008,0) | Sim | Campo Auxiliar 3 |
| CmpAu4 | Number(008,0) | Sim | Campo Auxiliar 4 |
| CmpAu5 | Number(008,0) | Sim | Campo Auxiliar 5 |
| CmpAu6 | Number(008,0) | Sim | Campo Auxiliar 6 |
| CmpAu7 | String(002) | Sim | Campo Auxiliar 7 |
| CmpAu8 | String(002) | Sim | Campo Auxiliar 8 |
| CmpAu9 | String(2000) | Sim | Campo Auxiliar 9 |
| TipEsc | Number(002,0) | Sim | Tipo de escolaridade |
| CodCbo | String(006) | Sim | Cbo do Cargo |

---

## Chave Primária

- NumEmp
- TipTxt
- NumTxt
- TipAtu
- TipQua
- CarFun
- DatIni
- TipEnv
- SeqReg

---

## Índices

### R304ACFIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
