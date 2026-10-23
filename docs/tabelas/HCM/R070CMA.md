# R070CMA

## Descrição

Marcações de acesso

---

## Resumo

- Campos: 32
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCra | String(012) | Sim | Número do Crachá |
| DiaAcc | String(002) | Sim | Data Acesso (dia) |
| MesAcc | String(002) | Sim | Data Acesso (mês) |
| AnoAcc | String(002) | Sim | Data Acesso (ano) |
| HorAcc | String(004) | Sim | Hora Acesso |
| SegAcc | String(002) | Sim | Sequência de acesso |
| TipAcc | String(003) | Sim | Tipo Acesso |
| DirAcc | String(001) | Sim | Direção Acesso |
| CodCen | String(002) | Sim | Código Central de Gerenciamento |
| CodRlg | String(002) | Sim | Número do terminal |
| NumEip | String(015) | Sim | Número do endereço IP do dispositivo |
| CodFnc | String(002) | Sim | Função da marcação |
| CraVei | String(015) | Sim | Crachá do veículo |
| StaRlg | String(002) | Sim | Status da Marcação |
| PesAcc | Number(005,3) | Sim | Quantidade (peso refeição) |
| ValAcc | Number(006,2) | Sim | Valor refeição |
| ValKil | Number(006,2) | Sim | Valor kilo refeição |
| QtdAcc | String(002) | Sim | Quantidade (sobremesa) |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| InfAdi | Number(005,0) | Sim | Informação Adicional |
| CraAut | String(012) | Sim | Número do crachá da pessoa autorizadora |
| FabMar | Number(002,0) | Sim | Fabricante |
| NumNSR | Number(009,0) | Sim | Número NSR |
| NumRep | String(017) | Sim | Número do REP |
| NumPis | Number(011,0) | Sim | Número do PIS/PASEP |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| Inform | String(299) | Sim | Informações do Registro |
| TipMar | String(001) | Sim | Tipo da Marcação |
| ValUsu | String(001) | Sim | Marcação validada pelo usuário |
| PlaVei | String(010) | Sim | Placa do Veículo |
| IMGLPR | Image | Sim | Imagem LPR |
| FusMar | Number(002,0) | Sim | Fuso Horário |

---

## Chave Primária

Não possui.

---

## Índices

### R070CMAIndice1

**Tipo:** Não unico

Campos:
- NumCra
- DiaAcc
- MesAcc
- AnoAcc
- HorAcc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
